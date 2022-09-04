FROM python:3.10.5

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
USER 1000:1000
COPY --chown=1000:1000 . /code
