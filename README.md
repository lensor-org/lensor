![CircleCI branch](https://img.shields.io/circleci/project/github/lensor-org/lensor/master.svg)
![GitHub issues](https://img.shields.io/github/issues/lensor-org/lensor.svg)
![CodeFactor](https://www.codefactor.io/repository/github/lensor-org/lensor/badge?style=flat-square)
![GitHub](https://img.shields.io/github/license/lensor-org/lensor.svg)

# Lensor

## Table of Contents

* [About](#about)
  * [Built With](#built-with)
* [Development Setup](#development-setup)
  * [Manually](#manually)
  * [Docker](#docker)
  * [VS Code Dev Container](#vs-code-dev-container)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## About

TODO Description

### Built with

TODO

## Development Setup

### Manually

> Note: On Windows we recommend using docker/vs code container, as face_recognition is not officially supported there.

1. Install Python3 including pip
2. Install pipenv with `pip install pipenv`
3. Install dlib as explained [here](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)
4. Run `pipenv install --dev` in the project directory.
5. Run `pipenv run prepare` after installing pipenv to install the git hook.
6. Start with `pipenv run python lensor.py`

### Docker

1. Install Docker
2. Start with `scripts/docker-dev.ps1` (Windows) / `scripts/docker-dev.sh` (Linux)

### VS Code Dev Container

1. Follow the official [installation instructions](https://code.visualstudio.com/docs/remote/containers#_installation)
2. Open the project in VS Code
3. Use `Ctrl + Shift + P` and run "Reopen Folder in Container"
5. Start with `pipenv run python lensor.py` (or open the `pipenv shell` and run `python main.py`)

## Usage

TODO Deployment & Docs

## Contributing

TODO

## License

MIT
