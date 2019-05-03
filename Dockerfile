############### 
#
# Development
#
###############
FROM kombustor/python3-dlib:alpine as dev

# Installing pipenv
RUN pip install pipenv

# Allowing to disable caching from here on by setting the CACHEBUST build-variable to a random value
ARG CACHEBUST=1

# Copying pipenv relevant files
WORKDIR /app
COPY ./Pipfile /app/
COPY ./Pipfile.lock /app/

# Installing dependencies to system python
RUN pipenv install --system --deploy --dev


############### 
#
# Production
#
###############
# FROM kombustor/python3-dlib 
# TODO extract python deps to requirements.txt and install via standard pip instead of creating a venv