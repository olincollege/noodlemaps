# syntax=docker/dockerfile:1
FROM python:3.7-alpine
# may want to swap out this for a different image? causes problems with matplotlib

WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# this may be bad for long term security but I don't understand enough about
# access points to know for sure

RUN apk add --no-cache gcc musl-dev linux-headers
# what does this line do? copied from the initial guide followed but not sure
# exactly what it does. Getting rid of it breaks things though so keep it

COPY docker/requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]