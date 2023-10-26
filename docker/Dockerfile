# pull official base image
FROM python:3.10-slim

# set work directory
WORKDIR /app3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
 && apt-get install -y tk tcl

# install dependencies
RUN pip install --upgrade pip
COPY /service_3/service_3/requirements.txt /app3/
RUN pip install -r requirements.txt

ADD /service_3/service_3 /app3/service3
ADD /service_3/docker /app3/docker
ADD /service_3/venv /app3/venv

RUN chmod +x /app3/docker/entrypoint.sh
RUN chmod +x /app3/docker/worker-entrypoint.sh