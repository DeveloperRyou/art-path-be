FROM python:3.12

COPY . /usr/server

WORKDIR /usr/server

RUN pip3 install -r requirements.txt

CMD ["fastapi", "run", "src/main.py", "--port", "80"]