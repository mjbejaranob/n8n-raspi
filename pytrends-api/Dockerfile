FROM python:3.10-slim
WORKDIR /app
COPY app.py /app
RUN pip install flask pytrends
EXPOSE 5000
CMD ["python", "app.py"]
