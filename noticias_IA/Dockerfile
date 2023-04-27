FROM python:latest
COPY . /IA_NEWS

RUN mkdir /manage
WORKDIR /manage
ADD . /manage
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python3", "manage.py", "runserver"]