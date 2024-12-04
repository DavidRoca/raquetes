# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /tennis_app

# Copy the project files into the container
COPY . /tennis_app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "tennis_app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]