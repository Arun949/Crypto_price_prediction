FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]