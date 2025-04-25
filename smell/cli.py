import click
from .version import VERSION

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