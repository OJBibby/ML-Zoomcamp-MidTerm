FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["train.py", "service.py", "insurance.csv", "./"]

RUN python "train.py"

EXPOSE 3000

ENTRYPOINT ["bentoml", "serve", "service.py:svc"]