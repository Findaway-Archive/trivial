# (generated with --quick)

from typing import Any

click: module
console: module
mock_wikipedia_random_page: Any
pytest: Any
requests: module
runner: Any

def test_main_prints_message_on_request_error(runner, mock_requests_get) -> None: ...
def test_main_prints_title(runner, mock_requests_get) -> None: ...
def test_main_succeeds(runner) -> None: ...
def test_main_uses_specified_language(runner, mock_wikipedia_random_page) -> None: ...
