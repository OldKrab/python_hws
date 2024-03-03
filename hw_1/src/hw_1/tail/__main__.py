from typing import List, TextIO
import click
import sys


def print_last_lines(file: TextIO, count: int):
    lines = file.readlines()
    for line in lines[-count:]:
        print(line, end="")


def handle_stdin():
    print_last_lines(sys.stdin, 17)


def handle_one_file(file: TextIO):
    print_last_lines(file, 10)


def handle_multiple_file(files: List[TextIO]):
    for (index, file) in enumerate(files):
        if index != 0:
            click.echo()
        click.echo(f"==> {file.name} <==")
        handle_one_file(file)


@click.command()
@click.argument("files", nargs=-1, type=click.File("r"))
def process_files(files: List[TextIO]):
    if not files:
        handle_stdin()
    elif len(files) == 1:
        handle_one_file(files[0])
    else:
        handle_multiple_file(files)


process_files()
