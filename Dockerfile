FROM python:3.7-alpine
WORKDIR /lab-cicd
COPY . .
RUN pip install -r requirements.txt