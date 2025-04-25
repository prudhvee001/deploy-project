# Use the official Python image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code
COPY . /app

# Expose the port that Flask uses (default is 5000)
EXPOSE 5000

# Command to run the app
CMD ["python", "attendance-service.py"]
