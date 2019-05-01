########################
#
# Base (python + dlib)
#
########################
FROM python:3-slim-stretch as base

# Installing dependencies
RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*


# Installing dlib
RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python setup.py install --yes USE_AVX_INSTRUCTIONS


############### 
#
# Development
#
###############
FROM base as dev
# Copying pipenv relevant files
COPY ./Pipfile /app/
COPY ./Pipfile.lock /app/
WORKDIR /app

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