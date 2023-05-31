# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the Docker image
COPY app/requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the Docker image
COPY app .

# Make port 8502 available to the world outside this container
EXPOSE 8502

# Set the entry point command to run the application
CMD ["streamlit", "run", "main.py", "--server.port=8502", "--server.address=0.0.0.0"]
