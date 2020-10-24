FROM python:3.6.1-alpine
n:3.6.1-alpine RUN pip install flask COPY app.py /app.py CMD ["python","app.py"]
RUN pip install flask
COPY app.py /app.py
CMD ["python","app.py"]
