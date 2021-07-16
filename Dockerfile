FROM python:3.8-slim-buster

# RUN mkdir /code
# WORKDIR /code
EXPOSE 5000
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# ENTRYPOINT ["python3"]
CMD ["flask", "run"]
#  "app.py"]