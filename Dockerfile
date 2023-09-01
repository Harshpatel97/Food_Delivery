FROM python:3.9
COPY . /app
WORKDIR /app
RUN apt update -y && apt install awscli -y
EXPOSE $PORT

CMD ["python3", "app.py"]