import pytest
from click.testing import CliRunner
from smell.cli import main

def test_version_command():
    runner = CliRunner()
    result = runner.invoke(main, ["version"])
    assert result.exit_code == 0
    assert result.output.strip() == "v0.1.0"

def test_version_option_v():
    runner = CliRunner()
    result = runner.invoke(main, ["-v"])
    assert result.exit_code == 0
    assert result.output.strip() == "v0.1.0"

def test_version_option_long():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert result.output.strip() == "v0.1.0"

def test_help_command():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Smell: A static code analysis tool for detecting code smells" in result.output
    assert "version  Display the current version of smell" in result.output

def test_help_option_h():
    runner = CliRunner()
    result = runner.invoke(main, ["-h"])
    assert result.exit_code == 0
    assert "Smell: A static code analysis tool for detecting code smells" in result.output
    assert "version  Display the current version of smell" in result.output

def test_version_help_command():
    runner = CliRunner()
    result = runner.invoke(main, ["version", "--help"])
    assert result.exit_code == 0
    assert "Display the current version of smell" in result.output