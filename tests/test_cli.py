import pytest
from click.testing import CliRunner
from smell.cli import main
from unittest.mock import patch, mock_open, MagicMock, Mock
from click.testing import CliRunner
from datetime import datetime
import git
from git.exc import GitCommandError

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

def test_analyze_invalid_repository():
    runner = CliRunner()
    with patch("git.Repo") as mock_repo:
        mock_repo.side_effect = git.InvalidGitRepositoryError("Not a Git repository")
        result = runner.invoke(main, ["analyze", "--branch", "main"])
        assert result.exit_code == 1
        assert "Error: Not a valid Git repository." in result.output

def test_analyze_branch_not_exist():
    runner = CliRunner()
    with patch("git.Repo") as mock_repo:
        mock_repo.return_value.git.checkout.side_effect = GitCommandError("checkout", 1, b"", b"error: pathspec 'nn' did not match any file")
        result = runner.invoke(main, ["analyze", "--branch", "nn"])
        assert result.exit_code == 1
        assert "Error: Branch 'nn' does not exist" in result.output

def test_analyze_code_smells():
    runner = CliRunner()
    mock_file = MagicMock()
    mock_file.parts = ["file.py"]
    mock_file.__str__.return_value = "file.py"

    # Mock open to return 10 lines
    mocked_open = mock_open(read_data="line\n" * 10)

    with patch("git.Repo") as mock_repo, \
         patch("pathlib.Path.rglob") as mock_rglob, \
         patch("pylint.lint.Run") as mock_pylint, \
         patch("builtins.open", mocked_open):

        mock_commit = Mock()
        mock_commit.committed_datetime = datetime(2025, 4, 25, 17, 44, 0)
        mock_commit.author.name = "Bater Chen"
        mock_commit.author.email = "baterme@gmail.com"
        mock_repo.return_value.head.commit = mock_commit
        mock_repo.return_value.git.checkout = Mock()

        mock_rglob.return_value = [mock_file]
        mock_pylint.return_value.linter.stats.global_note = 8

        result = runner.invoke(main, ["analyze", "--branch", "main"])

        assert result.exit_code == 0
        assert "Analyzing branch: main" in result.output
        assert "Python files: 1" in result.output
        assert "Total lines: 10" in result.output
        assert "Running code smell analysis..." in result.output
        assert "Code smells detected: 8/10" in result.output