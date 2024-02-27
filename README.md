# quarto-post-init

[![PyPI](https://img.shields.io/pypi/v/quarto-post-init.svg)](https://pypi.org/project/quarto-post-init/)
[![Changelog](https://img.shields.io/github/v/release/crossjam/quarto-post-init?include_prereleases&label=changelog)](https://github.com/crossjam/quarto-post-init/releases)
[![Tests](https://github.com/crossjam/quarto-post-init/workflows/Test/badge.svg)](https://github.com/crossjam/quarto-post-init/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/crossjam/quarto-post-init/blob/master/LICENSE)

Initialize a directory as a post for Quarto

## Installation

Install this tool using `pip`:

    pip install quarto-post-init

## Usage

For help, run:

    quarto-post-init --help

You can also use:

    python -m quarto_post_init --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd quarto-post-init
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
