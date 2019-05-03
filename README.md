![CircleCI branch](https://img.shields.io/circleci/project/github/Kombustor/lensor/master.svg)
![GitHub issues](https://img.shields.io/github/issues/Kombustor/lensor.svg)
![GitHub](https://img.shields.io/github/license/Kombustor/lensor.svg)

# Lensor

## Table of Contents

* [About](#about)
  * [Built With](#built-with)
* [Development Setup](#development-setup)
  * [Manually](#manually)
  * [Docker](#docker)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## About

TODO Description

### Built with

TODO

## Development Setup

### Manually

> Note: On Windows we recommend using docker, as face_recognition is not officially supported there.

1. Install Python3 including pip
2. Install pipenv with `pip install pipenv`
3. Install dlib as explained [here](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)
4. Run `pipenv install --dev` in the project directory.
5. Run `pipenv run prepare` after installing pipenv to install the git hook.
6. Start with `python main.py`

### Docker

1. Install Docker
2. Start with `scripts/docker-dev.ps1` (Windows) / `scripts/docker-dev.sh` (Linux)

## Usage

TODO Deployment & Docs

## Contributing

TODO

## License

MIT