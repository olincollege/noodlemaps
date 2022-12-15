# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./src/docker/requirements.txt ./src/docker/requirements.txt
RUN pip install -r ./src/docker/requirements.txt
EXPOSE 5000
COPY . .
#WORKDIR /frontend
#RUN python3 -m flask run
#CMD ["python3", "-m", "flask", "run"]
CMD ["flask", "run"]