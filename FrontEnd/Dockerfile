# Set base image (host OS)
FROM python:3.8-buster

# By default, listen on port 5000
EXPOSE 5000

# Set the working directory in the container
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

#RUN apk add --no-cache gcc musl-dev linux-headers

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# Install any dependencies
#RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
#CMD [ "python", "./app.py" ]