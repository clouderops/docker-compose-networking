FROM python:3.9

RUN pip3 install pipenv
ENV PROJECT_DIR /usr/src/api

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 5000

CMD ["pipenv", "run", "python3", "api.py"]