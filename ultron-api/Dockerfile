FROM python:3.7
WORKDIR /usr/app
COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
CMD python manage.py runserver 0.0.0.0:8000