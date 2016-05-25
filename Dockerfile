FROM python:3.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /uploads
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./flask_app /code/
