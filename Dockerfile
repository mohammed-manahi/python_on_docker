# Image
FROM python:3.10

# Display the Python output through the terminal
ENV PYTHONUNBUFFERED: 1

# Set work directory for docker image
WORKDIR /usr/src/app

# Add Python dependencies
RUN pip install --upgrade pip

# Copy requirements
COPY requirements.txt ./requirements.txt

# Install requirements
RUN pip3 install -r requirements.txt