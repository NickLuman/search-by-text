FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . . 

RUN pip install -r ./requirements/requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
