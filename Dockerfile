FROM python:3.11

ADD ./bank-accounts /home

ADD requirements.txt /home

RUN python -m pip install --upgrade pip

RUN python -m pip install -r /home/requirements.txt

ENTRYPOINT ["python", "/home", "-c", "10", "-a", "100"]