FROM python:3.8.10-slim
ENV PYTHONUNBUFFERED=1

# project directory
WORKDIR /app

# copy source files
COPY . /app

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt