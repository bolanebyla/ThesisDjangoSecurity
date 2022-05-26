FROM python:3.9


# set work directory
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

# create the app user
RUN addgroup app && useradd -g app app

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

 COPY run.sh .

# copy project
COPY . .

EXPOSE 8080

RUN chmod +x run.sh

# change to the app user
USER app

CMD ["./run.sh"]