FROM python:3.7
ADD . /app
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
