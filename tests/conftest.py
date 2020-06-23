"""Global testing tools."""
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    """Mocks a page summary returned from the Wikipedia API."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "According to all known laws of aviation...",
    }
    return mock
