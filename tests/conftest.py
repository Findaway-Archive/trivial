import pytest

from pytest_mock import MockFixture
from unittest.mock import Mock


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "According to all known laws of aviation...",
    }
    return mock
