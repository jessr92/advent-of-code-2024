from typing import TextIO


def read_all_of_file(filename: str) -> list[str]:
    file: TextIO = open(filename, "r")
    lines: list[str] = []
    for line in file:
        lines.append(line)
    return lines
