from typing import TextIO
import click


@click.command()
@click.argument("input_file", type=click.File("r"), default="-")
def nl(input_file: TextIO):
    for index, line in enumerate(input_file):
        click.echo(f"{index+1:6d}  {line}", nl=False)


nl()
