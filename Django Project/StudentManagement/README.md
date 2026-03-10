# Student Enrollment System

A modular Django 4.2 application to register students, add courses, and enroll students into courses. It includes a Google SMTP email integration to send HTML-styled acknowledgement emails to students upon successful enrollment. The frontend is built using Bootstrap 5 to deliver a modern and colorful UI.

## Features
- **Dashboard**: Get a quick overview of total students, active courses, and recent enrollments.
- **Register Students**: Simple and intuitive form to register new students.
- **Add Courses**: Form to add an academic course along with description and fees.
- **Enroll Students**: Enroll registered students into available courses.
- **Email Acknowledgement**: Automatically sends a modern, stylized HTML formatted email to the student using Google SMTP when enrolled.

## Setup Instructions

### 1. Database Configuration (MySQL)
The application expects a local MySQL server installed and running.
1. Open your MySQL client or phpMyAdmin and create a database:
   ```sql
   CREATE DATABASE student_enrollment_db;
   ```
2. By default, the app is configured to connect using user `root` with no password (`''`). If your MySQL server requires a password, please update it in `enrollment_system/settings.py` under the `DATABASES` section.

### 2. Email Configuration (Google SMTP)
To test the email functionality, you need to configure your Google SMTP credentials:
1. Go to your Google Account > Security > 2-Step Verification (turn it on) > App passwords.
2. Create an App password.
3. Open `enrollment_system/settings.py` and replace the email placeholders at the bottom of the file:
   ```python
   EMAIL_HOST_USER = 'your_email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your_app_password'
   ```

### 3. Migrate and Run
Once the database is created, open the `StudentManagement` directory in your terminal and run:

```bash
# Apply database migrations
python manage.py migrate

# Create a superuser to access the /admin dashboard (optional)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Done! Your application should now be accessible at `http://127.0.0.1:8000`.
