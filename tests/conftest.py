import pytest

@pytest.fixture
def mock_requests_get(mocker):
        mock = mocker.patch("requests.get")
        mock.return_value.__enter__.return_value.json.return_value = {
                "title": "Lorem Ipsum",
                "extract": "According to all known laws of aviation, there is no way the bee should be able to fly."
        }
        return mock
