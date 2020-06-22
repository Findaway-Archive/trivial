import click
import requests
import textwrap

from . import __version__

WIKI_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.version_option(version = __version__)

def main():
	"""Trivial, a project for pulling random Wikipedia articles."""
	with requests.get(WIKI_URL) as response:
		response.raise_for_status()
		data = response.json()

		title = data['title']
		extract = data['extract']

		click.secho(title, fg='green')
		click.echo(textwrap.fill(extract))