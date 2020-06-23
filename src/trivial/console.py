"""Script for managing the command line interface."""
import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """Displays a random Wikipedia page in the command line.

    Queries Wikipedia for a random article via wikipedia.py and displays it.

    Args:
        language: the language domain of Wikipedia to query.
    """
    page = wikipedia.random_page(language=language)

    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))
