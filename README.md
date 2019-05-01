# Lensor

## Table of Contents

* [About](#about)
  * [Built With](#built-with)
* [Development Setup](#development-setup)
  * [Dlib: Manually](#dlib-manually)
  * [Dlib: Docker](#dlib-docker)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## About

TODO Description

### Built with

TODO

## Development Setup

First, set the environment variable `PIPENV_VENV_IN_PROJECT=1`.
This will create the virtual environment under the project folder.

1. Install Python3 including pip
2. Install pipenv with `pip install pipenv`
3. Run `pipenv run prepare` after installing pipenv to install the git hook.
4. Run `pipenv install` in the project directory.

### Dlib: Manually

> Note: On Windows we recommend using docker, as face_recognition is not officially supported there.

1. Install dlib as explained [here](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)
2. Start with `python main.py`

### Dlib: Docker

1. Install Docker
2. Run `scripts/docker-dev.ps1` (Windows) / `scripts/docker-dev.sh` (Linux)

## Usage

TODO Deployment & Docs

## Contributing

TODO

## License

MIT