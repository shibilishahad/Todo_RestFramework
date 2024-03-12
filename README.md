# Todo-DRF-REST-Framework-
Django-based API for managing todos and categories. Secure user authentication, CRUD operations for tasks and categories. Boost productivity effortlessly.

# Technologies Used
Django: Web framework for building the application.
Django REST Framework: Toolkit for building Web APIs in Django.
Token Authentication: Token-based authentication for API endpoints.
SQLite: Database management system for storing application data.

# Setup
# Requirements:
 Python 3.x
 Django 5.0.x
 Django REST Framework 3.x

# Installation
1) Clone the repository:
git clone (https://github.com/SHADIMK7/Todo-DRF-REST-Framework-.git) - repo link
2) go to project directory:
3) pip install -r requirements.txt
4) Run database migrations using python manage.py migrate.
5) Start the Django development server using python manage.py runserver.

# Usage
## User Registration
To register a new user, send a POST request to /register/ endpoint with the following JSON:

{
    "username": "your_username",
    "password": "your_password"
}

After successful registration, you will receive a response containing a token that you can use for authentication.

## Authentication
To authenticate requests, include the token in the request headers as follows:

Authorization: Token <your_token>

## Todo Tasks
### Creating a Todo Task
Send a POST request to /todo/ endpoint with the following JSON:

{
    "title": "Task Title",
    "description": "Task Description",
    "due_date": "YYYY-MM-DD",
    "priority": "High/Medium/Low",
    "completed": false,
    "category": category_id
}

### Updating a Todo Task
Send a PUT request to /todo/<todo_id>/ endpoint with the updated JSON.

### Deleting a Todo Task
Send a DELETE request to /todo/<todo_id>/ endpoint.

## Categories
### Creating a Category
Send a POST request to /categories/ endpoint with the following JSON:

{
    "name": "Category Name",
    "description": "Category Description"
}


### Updating a Category
Send a PUT request to /category/<category_id>/ endpoint with the updated JSON.

### Deleting a Category
Send a DELETE request to /category/<category_id>/ endpoint.

# Additional Points:

Ensure to include the appropriate permissions for accessing certain endpoints. For example, only authenticated users can access todo tasks related endpoints. And users can see only their contents

For testing purposes, you can use the tool Postman to interact with the API endpoints.

# New Features Implemented: 

CRUD Operations for Categories: Added functionality to create, read, update, and delete categories.

User Authentication: Added a new field to the Todo model called "user" for user authentication. Users can only view, update, and delete their own todos.

Login, Registration, and Logout: Implemented endpoints for user authentication, including login, registration, and logout.

Token Authentication: Secured API endpoints with token-based authentication. Users need to include a token in their request headers for authentication.

Security Enhancement: Restricted access to todos based on user authentication. Only the user who created a todo can view, update, or delete it. Admins have exclusive rights to create categories.