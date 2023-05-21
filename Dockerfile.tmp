# Use the official Python image as the base image
FROM python:3.6-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY app_files .

# Expose the port that the FastAPI application will listen on
EXPOSE 5000

# Set the entrypoint command to run the app.py file using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]