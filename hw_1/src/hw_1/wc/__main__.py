import sys
from typing import List, TextIO, Tuple
import click
import os


def print_stat(lines: int, words: int, bytes: int, width: int, file_path: str | None = None):
    fmt = f"{lines:{width}} {words:{width}} {bytes:{width}}"
    if file_path is not None:
        fmt += f" {file_path}"
    click.echo(fmt)


def get_stat(file: TextIO) -> Tuple[int, int, int]:
    lines, words, bytes = 0, 0, 0
    for line in file:
        lines += line[-1] == "\n"[0] or line[-1] == b"\n"[0]
        words += len(line.split())
        bytes += len(line)
    return lines, words, bytes


def get_width(files: List[TextIO]) -> int:
    all_size = sum(os.path.getsize(file.name) for file in files)
    return len(str(all_size))


def handle_one_file(file: TextIO):
    print_stat(*get_stat(file), get_width([file]), file.name)


def handle_stdin():
    print_stat(*get_stat(sys.stdin), 7)


def handle_multiple_file(files: List[TextIO]):
    width = get_width(files)
    lines_sum, words_sum, bytes_sum = 0, 0, 0
    for file in files:
        lines, words, bytes = get_stat(file)
        lines_sum, words_sum, bytes_sum = lines_sum + lines, words_sum + words, bytes_sum + bytes
        print_stat(lines, words, bytes, width, file.name)
    print_stat(lines_sum, words_sum, bytes_sum, width, "total")


@click.command()
@click.argument("files", nargs=-1, type=click.File("rb"))
def process_files(files: List[TextIO]):
    if not files:
        handle_stdin()
    elif len(files) == 1:
        handle_one_file(files[0])
    else:
        handle_multiple_file(files)


process_files()
