############### 
#
# Development
#
###############
FROM kombustor/python3-dlib:stretch as dev

# Installing pipenv
RUN pip install pipenv

# Allowing to disable caching from here on by setting the CACHEBUST build-variable to a random value
ARG CACHEBUST=1

# Copying pipenv files
COPY ./Pipfile /app/
COPY ./Pipfile.lock /app/
WORKDIR /app

# Installing dependencies to system
RUN pipenv install --system --deploy --ignore-pipfile

############### 
#
# Production
#
###############
# FROM kombustor/python3-dlib 
# TODO extract python deps to requirements.txt and install via standard pip instead of creating a venv