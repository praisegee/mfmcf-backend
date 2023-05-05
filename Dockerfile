#############
### IMAGE ###
#############
FROM python:3.10-alpine3.16
LABEL maintainer="dayopraisegod@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY . /app

WORKDIR /app
EXPOSE 8000

# Create virtual environment, 
# install postgresql db and its dependencies
# then, install project requirements
# after create user and set as user
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip -r install /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        mfmcf-user

ENV PATH="/py/bin:$PATH"

USER mfmcf-user