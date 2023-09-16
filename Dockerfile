FROM python:3.9


RUN mkdir /code
WORKDIR /code

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

COPY requirements.txt /code/
RUN pip install -r requirements.txt
#COPY . /code/
# Use this command if you use bind mount
#WINDOWS: docker run --mount src=%cd%,target=/code,type=bind -p 8001:8000 -it --rm django-dev
#LINUX: docker run --mount src="${pwd}",target=/code,type=bind -p 8001:8000 -it --rm django-dev
CMD python manage.py runserver 0.0.0.0:8000