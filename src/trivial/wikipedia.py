import requests
import click


WIKI_URL = "https://{lang}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language):
    url = WIKI_URL.format(lang=language)
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
