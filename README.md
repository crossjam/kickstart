# kickstart

[![PyPI](https://img.shields.io/pypi/v/kickstart.svg)](https://pypi.org/project/kickstart/)
[![Changelog](https://img.shields.io/github/v/release/crossjam/kickstart?include_prereleases&label=changelog)](https://github.com/crossjam/kickstart/releases)
[![Tests](https://github.com/crossjam/kickstart/workflows/Test/badge.svg)](https://github.com/crossjam/kickstart/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/crossjam/kickstart/blob/master/LICENSE)

Initialize a directory as a post for Quarto

## Installation

Install this tool using `pip`:

    pip install git+https://github.com/crossjam/kickstart

## Usage

For help, run:

    kickstart --help

You can also use:

    python -m quarto_post_init --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd kickstart p
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
