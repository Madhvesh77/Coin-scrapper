# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /code/

# Set environment variables
ENV PYTHONUNBUFFERED=1

WORKDIR /code/coin_scraper/
# Default command to run the Celery worker
CMD ["celery", "-A", "coin_scraper", "worker", "--loglevel=info"]
