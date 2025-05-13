# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "main.py"]
