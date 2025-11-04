FROM python:3.9-slim

WORKDIR /application
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/

EXPOSE 8081

ENV PORT=8081

CMD ["python", "app.py"]
