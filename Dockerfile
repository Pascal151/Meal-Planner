# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV POETRY_VERSION=1.8.4 \
    POETRY_HOME=/opt/poetry \
    PATH="/opt/poetry/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies for Poetry and Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    python3-dev \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files to install dependencies
# COPY poetry.lock pyproject.toml /app/
COPY . /app/

# Install Python dependencies using Poetry
RUN poetry install --no-root --without dev

# Set environment variable for the host
RUN echo "\nDB_HOST='host.docker.internal'" >> /app/.env

# Expose the port your app runs on (optional)
EXPOSE 8000

# Set the command to run the application
CMD ["poetry", "run", "python", "main.py"]