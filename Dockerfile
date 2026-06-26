FROM python:3.9-slim
WORKDIR /app
RUN pip install flask requests gunicorn
COPY . .
CMD gunicorn -b 0.0.0.0:8080 main:app
