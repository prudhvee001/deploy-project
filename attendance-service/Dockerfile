FROM python:3.9-slim
WORKDIR /app
COPY . .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 3002
CMD ["python", "attendance-service.py"]
