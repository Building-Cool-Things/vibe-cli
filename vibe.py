import sys
import subprocess
import platform
import click
from command_actions.health import health_check


def detect_os():
    return platform.system()


# Configure Click
@click.group()
@click.version_option(
    version=2,
    package_name='vibe', # Optional: Name shown in --version output
    help="Show the version of the CLI tool and exit." # Help text for --version
)   
def cli():
    """
    VIBE
    """


# Commands
@cli.command() # Decorator to register 'check_health' as a subcommand of 'cli'
def health():
    """Performs a health check of VIBE"""
    
    result_message = health_check()
    if result_message:
        click.secho(health_check(), fg="green", bold=True)
        sys.exit(0)    
    else:
        click.secho("Health check failed or service is unreachable.", fg="red", bold=True)
        sys.exit(1)




if __name__ == "__main__":
    cli()