FROM python:3

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./app /app

ENTRYPOINT [ "python" ]

CMD [ "app/main.py" ]
