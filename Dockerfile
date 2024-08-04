#Use an official Python runtime as a parent image
FROM python:3.12.3-alpine

#set the working directory in the container
WORKDIR /app

#copy the requirements file into the container
COPY . /app

#install the dependencies
RUN pip install -r requirements.txt

#expose the port the app runs on
EXPOSE 5003

ENV FLASK_APP=app.py

#command to run the application 
CMD ["flask","run","--host=0.0.0.0","--port=5003"]