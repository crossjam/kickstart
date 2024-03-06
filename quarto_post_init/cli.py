import logging

from importlib import resources

import click
from cookiecutter.main import cookiecutter

from .logconfig import DEFAULT_LOG_FORMAT, logging_config

from . import templates


@click.group()
@click.version_option()
@click.option(
    "--log-format",
    type=click.STRING,
    default=DEFAULT_LOG_FORMAT,
    help="Python logging format string",
)
@click.option(
    "--log-level", default="ERROR", help="Python logging level", show_default=True
)
@click.option(
    "--log-file",
    help="Python log output file",
    type=click.Path(dir_okay=False, writable=True, resolve_path=True),
    default=None,
)
def cli(log_format, log_level, log_file):
    "Initialize a directory as a post for Quarto"

    logging_config(log_format, log_level, log_file)


@cli.command(name="post")
def post():
    """Create a new quarto post, from a template"""

    cookiecutters = []

    for p in resources.files(templates).iterdir():
        logging.info("Checking for template in %s", p)
        if (p / "cookiecutter.json").is_file():
            logging.info("cookiecutter template: %s", p)
            cookiecutters.append(p)

    click.echo(f"cookiecutter templates: {[str(v.name) for v in cookiecutters]}")
    cookiecutter(str(cookiecutters[0]))
