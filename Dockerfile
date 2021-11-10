# pull official base image
FROM python:3.7

RUN pip install --upgrade pip
# Install requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt


# set environment varibles
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV FLASK_APP run

# set working directory
COPY . /app
WORKDIR /app

CMD [ "uwsgi", "uwsgi.ini"]


