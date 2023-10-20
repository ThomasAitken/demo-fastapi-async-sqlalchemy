  
FROM python:3.11.4

RUN mkdir /backend
WORKDIR /backend

RUN apt update && \
    apt install -y postgresql-client

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .