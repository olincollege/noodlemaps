# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -r ./src/docker/requirements.txt
EXPOSE 5000
# Different environment, __init__ means pytest reads sys root as project root so then imports break
RUN rm __init__.py
CMD ["flask", "run"]