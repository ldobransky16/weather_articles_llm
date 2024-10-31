# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Set environment variables for Flask within the container
ENV FLASK_APP=${FLASK_APP}
ENV FLASK_ENV=${FLASK_ENV}

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
