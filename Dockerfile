FROM python:3.12-alpine

EXPOSE 5000/tcp

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["flask", "run", "--host=0.0.0.0"]

#testing pull on vps