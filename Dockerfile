from python:3.7-alpine
MAINTAINER London App Developer Ltd

# RUN python on unbeffered mode.. 
ENV PYTHONUNBEFFERED 1
# copy the dependencies from requirements.text
COPY ./requirements.txt /requirements.txt
# install and run dependencies
RUN pip install -r /requirements.txt
# create a folder app into docker.. Main location
RUN mkdir/app
WORKDIR /app
COPY ./app /app
# create a user for run our system app. For security purpose of our image
RUN adduser -D user
USER user
