FROM kombustor/python3-dlib:stretch

# Copy default endpoint specific user settings overrides into container to specify Python path
COPY .devcontainer/settings.vscode.json /root/.vscode-remote/data/Machine/settings.json

# Installing pipenv
RUN pip install pipenv

ENV PIPENV_VENV_IN_PROJECT=1