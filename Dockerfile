# Use the official Python image as the base image
FROM python:3.6-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py file to the working directory
COPY app_files/app.py .

# Expose the port on which the FastAPI application will run
EXPOSE 5000

# Start the FastAPI application using Uvicorn server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]