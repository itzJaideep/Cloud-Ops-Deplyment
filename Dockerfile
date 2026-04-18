FROM python:3.12-slim

WORKDIR /app

COPY hello.py /app/

RUN pip install flask

EXPOSE 5000

CMD ["python", "hello.py"]
