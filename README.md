# Flask User Management App

A simple Flask web application for managing user data with full CRUD (Create, Read, Update, Delete) functionality. The app provides a clean web interface for adding, viewing, editing, and deleting user records stored in a SQLite database.

![Screenshot 2024-04-04 134152](https://github.com/RahulGupta931/Flask-CRUD-Project/assets/113452509/5b274913-cd61-4817-984f-cd412abb2388)

![Screenshot 2024-04-04 134342](https://github.com/RahulGupta931/Flask-CRUD-Project/assets/113452509/2b001c89-ee57-45e4-b8a4-44d746c75ea0)

![Screenshot 2024-04-04 134358](https://github.com/RahulGupta931/Flask-CRUD-Project/assets/113452509/38942437-43ea-4f88-bd88-ace21edb4508)


## Features

- **Add Users**: Create new user records with first name, last name, phone number, and address
- **View Users**: Display all users in a responsive table format
- **Edit Users**: Update existing user information through a popup modal
- **Delete Users**: Remove users with confirmation dialog
- **Responsive Design**: Clean, modern UI that works on different screen sizes
- **Database Migrations**: Alembic integration for database schema management

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Migrations**: Flask-Migrate with Alembic
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design

## Project Structure

```
├── app.py                 # Main Flask application
├── requirments.txt        # Python dependencies
├── instance/
│   └── mydb.sqlite3      # SQLite database file
├── migrations/           # Database migration files
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   └── versions/
├── static/
│   ├── css/
│   │   └── styles.css    # Main stylesheet
│   ├── js/
│   │   └── script.js     # JavaScript functionality
│   └── media/            # Media files directory
└── templates/
    ├── home.html         # Add user form page
    └── index.html        # User list and management page
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flask-user-management
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirments.txt
   ```

4. **Install additional required packages**
   ```bash
   pip install flask-sqlalchemy flask-migrate
   ```

5. **Initialize the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Access the application**
   Open your web browser and navigate to `http://localhost:5000`

3. **Using the application**
   - **Home Page** (`/`): Add new users using the form
   - **User List** (`/index`): View all users, edit or delete existing records

## API Endpoints

- `GET /` - Display the add user form
- `POST /` - Create a new user
- `GET /index` - Display all users
- `POST /edit/<id>` - Update user with specified ID
- `POST /delete/<id>` - Delete user with specified ID

## Database Schema

The application uses a simple User model with the following fields:

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(100), nullable=False)
```

## Features in Detail

### User Interface
- **Dark theme** with clean, modern design
- **Responsive layout** that adapts to different screen sizes
- **Interactive modals** for editing and deleting users
- **Form validation** to ensure required fields are filled

### Backend Functionality
- **SQLAlchemy ORM** for database operations
- **Flask-Migrate** for database schema versioning
- **Error handling** with 404 responses for missing users
- **Session management** for database transactions

## Development

### Running in Development Mode
The application runs in debug mode by default, which provides:
- Automatic reloading on code changes
- Detailed error messages
- Interactive debugger

### Database Migrations
To create a new migration after model changes:
```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- Add user authentication and authorization
- Implement search and filtering functionality
- Add data validation and error handling
- Include user profile pictures
- Add export functionality (CSV, PDF)
- Implement pagination for large datasets
- Add unit tests and integration tests

## Troubleshooting

### Common Issues

1. **Database not found**: Run `flask db upgrade` to create the database
2. **Module not found**: Ensure all dependencies are installed with `pip install -r requirments.txt`
3. **Port already in use**: Change the port in `app.py` or stop other Flask applications

### Support

For issues and questions, please create an issue in the repository or contact the development team.
