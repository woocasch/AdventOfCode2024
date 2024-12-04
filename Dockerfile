# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script and requirements file into the container
COPY script.py /app/script.py
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the script
CMD ["python", "script.py"]