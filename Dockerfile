FROM python:3.8

RUN mkdir -p /home/app

COPY . /home/app

RUN pip install -r /home/app/requirements.txt

CMD ["python" , "/home/app/main.py"]

ENTRYPOINT ["tail", "-f", "/dev/null"]