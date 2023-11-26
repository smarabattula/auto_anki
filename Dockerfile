# syntax=docker/dockerfile:1

FROM python:latest

WORKDIR /auto_anki

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update -y
RUN apt-get install tk -y
RUN python -m spacy download en_core_web_lg
RUN cd ..

COPY . .
EXPOSE 5000

CMD [ "python3" , "code/ui1.py", "--host", "0.0.0.0", "--port", "5000"]