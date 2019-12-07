FROM python:3.7
WORKDIR /usr/app
COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
