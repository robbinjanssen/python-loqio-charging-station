_Asynchronous Python client for the Loqio Charging Station API._

## About

A python package with which you can read the data from your Loqio Charging Station.

## Installation

```bash
pip install python-loqio-charging-station
```

## Usage

```python
# todo
```

## Use cases

_todo_

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

This Python project is fully managed using the [Poetry][poetry] dependency
manager.

You need at least:

- Python 3.9+
- [Poetry][poetry-install]

Install all packages, including all development requirements:

```bash
poetry install
```

Poetry creates by default an virtual environment where it installs all
necessary pip packages, to enter or exit the venv run the following commands:

```bash
poetry shell
exit
```

Setup the pre-commit check, you must run this inside the virtual environment:

```bash
pre-commit install
```

*Now you're all set to get started!*

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/robbinjanssen/python-loqio-charging-station/actions/workflows/tests.yaml/badge.svg
[build-url]: https://github.com/robbinjanssen/python-loqio-charging-station/actions/workflows/tests.yaml
[code-quality-shield]: https://github.com/robbinjanssen/python-loqio-charging-station/actions/workflows/codeql.yaml/badge.svg
[code-quality]: https://github.com/robbinjanssen/python-loqio-charging-station/actions/workflows/codeql.yaml
[commits-shield]: https://img.shields.io/github/commit-activity/y/robbinjanssen/python-loqio-charging-station.svg
[commits-url]: https://github.com/robbinjanssen/python-loqio-charging-station/commits/main
[codecov-shield]: https://codecov.io/gh/robbinjanssen/python-loqio-charging-station/branch/main/graph/badge.svg?token=VQTR24YFQ9
[codecov-url]: https://codecov.io/gh/robbinjanssen/python-loqio-charging-station
[downloads-shield]: https://img.shields.io/pypi/dm/loqio-charging-station
[downloads-url]: https://pypistats.org/packages/loqio-charging-station
[issues-shield]: https://img.shields.io/github/issues/robbinjanssen/python-loqio-charging-station.svg
[issues-url]: https://github.com/robbinjanssen/python-loqio-charging-station/issues
[license-shield]: https://img.shields.io/github/license/robbinjanssen/python-loqio-charging-station.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/robbinjanssen/python-loqio-charging-station.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg
[maintainability-shield]: https://api.codeclimate.com/v1/badges/ec5166b74a63f375d1a1/maintainability
[maintainability-url]: https://codeclimate.com/github/robbinjanssen/python-loqio-charging-station/maintainability
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[pypi]: https://pypi.org/project/loqio-charging-station/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/loqio-charging-station
[releases-shield]: https://img.shields.io/github/release/robbinjanssen/python-loqio-charging-station.svg
[releases]: https://github.com/robbinjanssen/python-loqio-charging-station/releases
[stars-shield]: https://img.shields.io/github/stars/robbinjanssen/python-loqio-charging-station.svg
[stars-url]: https://github.com/robbinjanssen/python-loqio-charging-station/stargazers

[energiewacht]: https://www.energiewacht.com/hoofdsite/home/nieuws/omnik-failliet/
[omnik-inverter]: https://github.com/robbinjanssen/home-assistant-omnik-inverter
[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
