import click.testing
import pytest

from trivial import console

#@pytest.fixture
#def runner():
#	return click.testing.CliRunner()

def test_main_succeeds():
	runner = click.testing.CliRunner()
	result = runner.invoke(console.main)
	assert result.exit_code == 0
