Bookstore API
This is a RESTful API for an online bookstore built with Django and Django Rest Framework. It handles operations related to books, authors, customers, and orders.
Features

CRUD operations for books, authors, and customers
Order placement with first-time customer discount
Authentication and authorization for authors and customers
Search and filtering for books by title, author, price, and publication date

Prerequisites

Python 3.9 or higher
DBSQLITe
Docker (optional)

Setup

Clone the repository

Create a virtual environment and activate it:
Copypython -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:
Copypip install -r requirements.txt

Set up the PostgreSQL database:

Create a new database named bookstore_db
Update the database configuration in bookstore_api/settings.py


Set up environment variables:
Create a .env file in the project root and add the following:
CopyDATABASE_URL=postgresql://user:password@localhost:5432/bookstore_db
DISCOUNT_TYPE=PERCENTAGE
DISCOUNT_VALUE=10

Run database migrations:
Copypython manage.py migrate

Create a superuser:
Copypython manage.py createsuperuser

Run the development server:
Copypython manage.py runserver


The API will be available at http://localhost:8000/api/.
Docker Setup

Build the Docker image:
Copydocker build -t bookstore-api .

Run the Docker container:
Copydocker run -p 8000:8000 -e DATABASE_URL=postgresql://user:password@host.docker.internal:5432/bookstore_db bookstore-api


API Documentation
The full API documentation is available as a Postman collection. You can download it here.
Main Endpoints

Books: /api/books/
Authors: /api/authors/
Customers: /api/customers/
Orders: /api/orders/
Place Order: /api/orders/place_order/

Authentication
The API uses token-based authentication. To obtain a token, send a POST request to /api/token/ with your username and password.
Include the token in the Authorization header of your requests:
CopyAuthorization: Token <your-token>
Testing
To run the test suite:
Copypython manage.py test
