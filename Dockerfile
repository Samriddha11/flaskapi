# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install necessary packages
RUN apt-get update && \
    apt-get install -y curl ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

# Copy the application code to the container
COPY app.py ./

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8989 (Flask default)
EXPOSE 8989

# Run the application
CMD ["python", "app.py"]
