from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from app import db
from app.models import User, Task
from app.forms import LoginForm, RegisterForm, TaskForm

# Create blueprints
main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

# Authentication routes
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid username or password')
    
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if user already exists
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exists')
            return render_template('register.html', form=form)
        
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered')
            return render_template('register.html', form=form)
        
        # Create new user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Main application routes
@main.route('/')
@login_required
def dashboard():
    # Get filter parameters
    status_filter = request.args.get('status', 'all')
    search = request.args.get('search', '')
    
    # Build query
    query = Task.query.filter_by(user_id=current_user.id)
    
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
    
    if search:
        query = query.filter(Task.title.contains(search) | Task.description.contains(search))
    
    tasks = query.order_by(Task.created_at.desc()).all()
    
    # Get statistics
    total_tasks = Task.query.filter_by(user_id=current_user.id).count()
    pending_tasks = Task.query.filter_by(user_id=current_user.id, status='pending').count()
    completed_tasks = Task.query.filter_by(user_id=current_user.id, status='completed').count()
    high_priority_tasks = Task.query.filter_by(user_id=current_user.id, priority='high').count()
    
    stats = {
        'total': total_tasks,
        'pending': pending_tasks,
        'completed': completed_tasks,
        'high_priority': high_priority_tasks
    }
    
    return render_template('dashboard.html', tasks=tasks, stats=stats, 
                         current_filter=status_filter, search_term=search)

@main.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            category=form.category.data,
            due_date=form.due_date.data,
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully!')
        return redirect(url_for('main.dashboard'))
    
    return render_template('task_form.html', form=form, title='Add New Task')

@main.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    form = TaskForm(obj=task)
    
    if form.validate_on_submit():
        form.populate_obj(task)
        task.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Task updated successfully!')
        return redirect(url_for('main.dashboard'))
    
    return render_template('task_form.html', form=form, title='Edit Task')

@main.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!')
    return redirect(url_for('main.dashboard'))

@main.route('/toggle_task/<int:task_id>', methods=['POST'])
@login_required
def toggle_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    task.status = 'completed' if task.status == 'pending' else 'pending'
    task.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify({'status': task.status})