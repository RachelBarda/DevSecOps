FROM python:3.8-alpine


COPY ./requirements.txt /app/requirements.txt
COPY ./src/myflask.py   /app/myflask.py


WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["myflask.py"]

