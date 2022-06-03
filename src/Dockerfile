FROM python:3.9


# set work directory
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

# create the app user
RUN addgroup app && useradd -g app app

RUN apt update && apt install -y netcat

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV SECRET_KEY build

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY run.sh .


COPY check_db.sh .

# copy project
COPY . .

EXPOSE 8080

RUN chmod +x check_db.sh
RUN chmod +x run.sh

# change to the app user
USER app

RUN python manage.py collectstatic --noinput
ENV SECRET_KEY=

ENTRYPOINT ["./check_db.sh"]

CMD ["./run.sh"]