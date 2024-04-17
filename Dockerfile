FROM ubuntu

COPY . /home/Desktop/forum/example
WORKDIR /home/Desktop/forum/example

RUN apt-get update && apt-get install -y python3 && apt install -y python3-psycopg2 && apt-get install -y python3-flask && apt-get install -y gunicorn3

CMD ["python3","app.py"]
