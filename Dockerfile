FROM python:3.9-slim
RUN pip install psutil
WORKDIR /monitor/one_project
COPY monitor.py .
CMD ["python", "monitor.py"]