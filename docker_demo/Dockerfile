# parent image, alpine is a lightweight linux distribution
FROM alpine:latest

# run command line to install bash
RUN apk update && apk add bash

# set working directory
WORKDIR /app

# copy files from host to container
COPY repeat.sh /app