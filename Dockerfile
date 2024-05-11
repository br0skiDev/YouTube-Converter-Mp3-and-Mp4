FROM python:3.9

ADD main.py .
ADD requirements.txt .
ADD .env .

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]