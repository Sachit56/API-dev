FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

COPY wait.sh /app/wait.sh

RUN chmod +x /app/wait.sh

EXPOSE 8000

CMD ["./wait.sh"]
