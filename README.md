# Task Management System

A comprehensive web-based task management application built with Flask, designed to help users organize, track, and manage their daily tasks efficiently.

##  Features

### Core Functionality
- **User Authentication**: Secure registration and login system
- **Task Management**: Create, read, update, and delete tasks
- **Task Categorization**: Organize tasks by categories (Work, Personal, Shopping, Health)
- **Priority Levels**: Set task priorities (High, Medium, Low) with color coding
- **Status Tracking**: Mark tasks as pending or completed
- **Due Date Management**: Set and track task deadlines
- **Search & Filter**: Find tasks by title/description and filter by status
- **Dashboard Statistics**: Visual overview of task counts and priorities

### User Interface
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Bootstrap Integration**: Modern, clean, and professional interface
- **Interactive Elements**: Hover effects, smooth transitions, and intuitive navigation
- **Color-Coded System**: Visual indicators for priorities and categories
- **Real-time Updates**: Instant task status changes with AJAX

##  Technologies Used

### Backend
- **Flask 2.3.3**: Python web framework
- **SQLAlchemy**: Database ORM for data management
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and validation
- **Werkzeug**: WSGI utilities and password hashing

### Frontend
- **HTML5 & CSS3**: Modern web standards
- **Bootstrap 5.1.3**: Responsive CSS framework
- **Font Awesome 6.0**: Icon library
- **jQuery 3.6.0**: JavaScript library for interactivity

### Database
- **SQLite**: Lightweight database for development
- **Database Relationships**: User-Task one-to-many relationship

##  Project Structure

```
Task_Management_system/
├── app/
│   ├── __init__.py          # Application factory and configuration
│   ├── models.py            # Database models (User, Task)
│   ├── routes.py            # Route handlers and business logic
│   ├── forms.py             # WTForms form definitions
│   └── static/
│       └── style.css        # Custom CSS styles
├── templates/
│   ├── base.html            # Base template with navigation
│   ├── login.html           # User login page
│   ├── register.html        # User registration page
│   ├── dashboard.html       # Main dashboard with tasks
│   └── task_form.html       # Task creation/editing form
├── instance/                # Instance-specific files
├── venv/                    # Virtual environment
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── README.md               # Project documentation
```

##  Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Task_Management_system
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**
   ```bash
   python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all(); print('Database initialized successfully!')"
   ```

5. **Run the Application**
   ```bash
   python run.py
   ```

6. **Access the Application**
   - Open your web browser
   - Navigate to `http://127.0.0.1:5000`
   - Register a new account or login

##  Usage Guide

### Getting Started
1. **Register**: Create a new account with username, email, and password
2. **Login**: Access your personal dashboard
3. **Add Tasks**: Click "Add New Task" to create your first task
4. **Manage Tasks**: Edit, complete, or delete tasks as needed
5. **Filter & Search**: Use the search bar and status filters to find specific tasks

### Task Management
- **Creating Tasks**: Fill in title (required), description, priority, category, and due date
- **Editing Tasks**: Click the "Edit" button on any task card
- **Completing Tasks**: Use the "Complete" button to mark tasks as done
- **Deleting Tasks**: Click "Delete" to permanently remove tasks

### Dashboard Features
- **Statistics Cards**: View total, pending, completed, and high-priority task counts
- **Task Cards**: Visual representation of each task with all relevant information
- **Filtering**: Filter tasks by status (All, Pending, Completed)
- **Search**: Find tasks by searching title or description content

##  Database Schema

### User Model
```python
- id: Primary key
- username: Unique username
- email: User email address
- password_hash: Encrypted password
- created_at: Account creation timestamp
- tasks: Relationship to user's tasks
```

### Task Model
```python
- id: Primary key
- title: Task title (required)
- description: Task description (optional)
- priority: Priority level (low/medium/high)
- status: Task status (pending/completed)
- category: Task category (personal/work/shopping/health)
- due_date: Task deadline (optional)
- created_at: Task creation timestamp
- updated_at: Last modification timestamp
- user_id: Foreign key to User
```

##  Features Overview

### Authentication System
- Secure user registration with form validation
- Password hashing using Werkzeug
- Session management with Flask-Login
- Protected routes requiring authentication

### Task Operations
- **Create**: Add new tasks with comprehensive details
- **Read**: View all tasks in organized dashboard
- **Update**: Edit existing task information
- **Delete**: Remove unwanted tasks with confirmation

### User Experience
- **Responsive Design**: Optimized for all screen sizes
- **Visual Feedback**: Color-coded priorities and status indicators
- **Interactive UI**: Smooth animations and hover effects
- **Form Validation**: Client and server-side validation
- **Flash Messages**: User feedback for all operations

##  Security Features

- **Password Hashing**: Secure password storage
- **CSRF Protection**: Form security with Flask-WTF
- **Session Management**: Secure user sessions
- **Input Validation**: Server-side form validation
- **User Authorization**: Access control for user-specific data

##  Deployment Considerations

### For Production Deployment:
1. **Environment Variables**: Use environment variables for sensitive configuration
2. **Database**: Switch to PostgreSQL or MySQL for production
3. **WSGI Server**: Use Gunicorn or uWSGI
4. **Reverse Proxy**: Configure Nginx for static files and SSL
5. **Security**: Enable HTTPS and configure security headers

### Environment Configuration:
```python
# Production settings
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
```

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

##  Future Enhancements

### Potential Features
- **Email Notifications**: Reminders for due tasks
- **Task Comments**: Add notes and comments to tasks
- **File Attachments**: Upload files to tasks
- **Task Sharing**: Collaborate with other users
- **Calendar View**: Visual calendar interface
- **Export Options**: PDF and CSV export functionality
- **Dark Mode**: Theme switching capability
- **Mobile App**: React Native or Flutter mobile version

##  Troubleshooting

### Common Issues

**Database Errors:**
```bash
# Reset database
rm instance/tasks.db
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
```

**Template Not Found:**
- Ensure templates are in the `templates/` folder at project root
- Check template names in route handlers

**Import Errors:**
- Verify virtual environment is activated
- Reinstall requirements: `pip install -r requirements.txt`

**Port Already in Use:**
- Change port in run.py: `app.run(debug=True, port=5001)`

##  Acknowledgments

- Flask documentation and community
- Bootstrap for the responsive framework
- Font Awesome for the icon library
- SQLAlchemy for database management
- All contributors and testers

---

