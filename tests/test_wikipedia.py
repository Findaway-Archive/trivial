"""Unit tests for wikipedia.py."""
from unittest.mock import Mock

import click
import pytest

from trivial import wikipedia


def test_random_page_uses_given_language(mock_requests_get: Mock):
    """It queries the Wikipedia language domain requested."""
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_requests_get: Mock):
    """It returns a Page object."""
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_errors(mock_requests_get: Mock) -> None:
    """It exits gracefully when Wikipedia provides an invalid page."""
    mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(click.ClickException):
        wikipedia.random_page()
