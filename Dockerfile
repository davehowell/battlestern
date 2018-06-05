FROM python:3.6.5-stretch

SHELL ["/bin/bash", "-c"]

COPY ./requirements.txt /opt/battlestern/requirements.txt

WORKDIR /opt/battlestern

RUN pip install virtualenv

RUN virtualenv ./venv --no-site-packages

RUN source ./venv/bin/activate

RUN pip install -r requirements.txt

COPY ./src/battlestern /opt/battlestern/src/battlestern

COPY ./tests /opt/battlestern/tests


#CMD [ "python", "./battlestern/ships.py"]
CMD [ "entrypoint.sh"]