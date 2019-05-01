############### 
#
# Development
#
###############
FROM kombustor/python3-dlib as dev

# Copying pipenv relevant files
COPY ./Pipfile /app/
COPY ./Pipfile.lock /app/
WORKDIR /app

RUN apk add jpeg-dev zlib-dev

# Installing pipenv
RUN pip install pipenv

# Allowing to disable caching from here on
ARG CACHEBUST=1

# Installing dependencies to system python
RUN pipenv install --system --deploy


############### 
#
# Production
#
###############
FROM base as prod 
# TODO