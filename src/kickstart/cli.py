import logging

from importlib import resources

import click
from cookiecutter.main import cookiecutter

import questionary

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
    """A tool for kickstarting web content writing"""

    logging_config(log_format, log_level, log_file)


@cli.command(name="init")
@click.option("--replay / --no-replay", default=False)
def init(replay):
    """Initialize new content from a cookiecutter template"""

    cookiecutters = {}

    for p in resources.files(templates).iterdir():
        logging.info("Checking for template in %s", p)
        if (p / "cookiecutter.json").is_file():
            logging.info("cookiecutter template: %s", p)
            cookiecutters[p.name] = p

    click.echo(f"cookiecutter templates: {[v for v in cookiecutters.keys()]}")

    choice = questionary.select(
        "Choose a post template", choices=list(cookiecutters.keys())
    ).ask()

    cookiecutter(str(cookiecutters[choice]), replay=replay)


@cli.command(name="templates")
def list_templates():
    """List the available templates"""

    cookiecutters = {}

    for p in resources.files(templates).iterdir():
        logging.info("Checking for template in %s", p)
        if (p / "cookiecutter.json").is_file():
            logging.info("cookiecutter template: %s", p)
            cookiecutters[p.name] = p

    click.echo(f"{len(cookiecutters)} templates")

    for name, location in cookiecutters.items():
        click.echo(f"\t{name} -> {str(location)}")
