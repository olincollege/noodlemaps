# syntax=docker/dockerfile:1

# may want to swap out this for a different image? causes problems with matplotlib
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=src/app.py
# this may be bad for long term security but I don't understand enough about
# access points to know for sure
ENV FLASK_RUN_HOST=0.0.0.0

# what does this line do? copied from the initial guide followed but not sure
# exactly what it does. Getting rid of it breaks things though so keep it
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -r ./src/docker/requirements.txt
EXPOSE 5000
# Different environment, __init__ means pytest reads sys root as project root so then imports break
RUN rm __init__.py
CMD ["flask", "run"]