"""Wikipedia REST API client."""
from dataclasses import dataclass

import click
import desert
import marshmallow
import requests


@dataclass
class Page:
    """Represents a Wikipedia page overview.

    Attributes:
        title: the title of the page.
        extract: a summary of the page's contents.
    """

    title: str
    extract: str


schema = desert.schema(Page, meta={"unknown": marshmallow.EXCLUDE})

WIKI_URL: str = "https://{lang}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language: str = "en") -> Page:
    """Get the contents of a random Wikipedia page.

    Queries the /page/random/summary endpoint of the Wikipedia REST API.

    Args:
        language: the Wikipedia language domain to use.

    Returns:
        a Page representing a random Wikipedia article.

    Raises:
        ClickException: The query failed, or received an invalid response.

    Example:
        >>> from hypermodern_python import wikipedia
        >>> page = wikipedia.random_page(language="en")
        >>> bool(page.title)
        True
    """
    url = WIKI_URL.format(lang=language)
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            data = response.json()
            return schema.load(data)
    except (requests.RequestException, marshmallow.ValidationError) as error:
        message = str(error)
        raise click.ClickException(message)
