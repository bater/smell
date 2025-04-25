import click
from .version import VERSION
import pylint.lint
import git
from git.exc import GitCommandError
from pathlib import Path

@click.group(
    help="Smell: A static code analysis tool for detecting code smells.\n\n"
         "Use this tool to analyze your codebase and identify potential issues.",
    add_help_option=True,  # Explicitly enable --help/-h
    context_settings={"help_option_names": ["-h", "--help"]}  # Ensure -h is an alias
)
@click.version_option(VERSION, "-v", "--version", message="%(version)s")
def main():
    """A static code analysis tool for detecting code smells."""
    pass

@main.command(
    name="version",
    help="Display the current version of smell."
)
def version():
    """Display the version of smell."""
    click.echo(VERSION)

@main.command()
@click.option("--branch", default="main", help="Git branch to analyze")
def analyze(branch):
    """Analyze code smells in the specified branch."""
    try:
        repo = git.Repo(".")
        try:
            repo.git.checkout(branch)
        except GitCommandError as e:
            click.echo(f"Error: Branch '{branch}' does not exist or could not be checked out.", err=True)
            click.get_current_context().exit(1)

        commit = repo.head.commit
        commit_datetime = commit.committed_datetime.strftime("%Y-%m-%d %H:%M:%S")
        author = f"{commit.author.name} <{commit.author.email}>"
        click.echo(f"Analyzing branch: {branch}")
        click.echo(f"Last commit: {commit_datetime} by {author}")

        # Collect Python files and count lines
        python_files = []
        total_lines = 0
        for file in Path(".").rglob("*.py"):
            if not any(part.startswith(".") for part in file.parts):  # Exclude hidden dirs
                python_files.append(str(file))
                with open(file, "r", encoding="utf-8") as f:
                    total_lines += sum(1 for _ in f)

        click.echo(f"Python files: {len(python_files)}")
        click.echo(f"Total lines: {total_lines}")

        if python_files:
            click.echo("Running code smell analysis...")
            pylint_args = [
                "--disable=all", "--enable=too-many-locals,too-many-branches",
                "--output-format=text", *python_files
            ]
            run = pylint.lint.Run(pylint_args, exit=False)
            click.echo(f"Code smells detected: {run.linter.stats.global_note}/10")
        else:
            click.echo("No Python files to analyze.")
    except git.InvalidGitRepositoryError:
        click.echo("Error: Not a valid Git repository.", err=True)
        click.get_current_context().exit(1)
    except git.NoSuchPathError:
        click.echo(f"Error: Branch {branch} does not exist.", err=True)
        click.get_current_context().exit(1)
