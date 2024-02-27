import logging

import click

from .logconfig import DEFAULT_LOG_FORMAT, logging_config


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


@cli.command(name="command")
@click.argument("example")
def first_command(example):
    "Command description goes here"

    click.echo("Here is some output")
    logging.info("Here's some log output")
