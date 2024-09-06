# Use the appropriate Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . /app

# Automatically apply migrations and run the Django development server
CMD ["sh", "-c", "python myproject/manage.py migrate && python myproject/manage.py runserver 0.0.0.0:8000 --noreload"]
