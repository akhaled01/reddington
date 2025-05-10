import click
from .dispatch import dispatch
from rich.traceback import install

install()

@click.command()
@click.argument('command')
@click.argument('value', required=False)
def main(command, value):
    dispatch([command, value] if value else [command])

if __name__ == "__main__":
    main()
