"""Unit tests for console.py."""
from unittest.mock import Mock

import click.testing
from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture
import requests

from trivial import console


@pytest.fixture
def runner() -> CliRunner:
    """A test command line environment."""
    return click.testing.CliRunner()


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    """Stands in for a random page object."""
    return mocker.patch("trivial.wikipedia.random_page")


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of 0."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It prints the title of a random page."""
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_prints_message_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    """It prints errors when they occur."""
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


def test_main_uses_specified_language(
    runner: CliRunner, mock_wikipedia_random_page: Mock
) -> None:
    """It queries the language domain passed into it."""
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")
