import re
from functools import reduce


def part_1(program: list[str]) -> int:
    total: int = 0
    for instructions in program:
        multiplications: list[str] = re.findall("mul\(\d+,\d+\)", instructions)
        total += reduce(lambda x, y: x + multiply(y), multiplications, 0)
    return total


def part_2(program: list[str]) -> int:
    total: int = 0
    multiplication_enabled = True
    for instructions in program:
        instruction_list: list[str] = re.findall("do\(\)|don't\(\)|mul\(\d+,\d+\)", instructions)
        for instruction in instruction_list:
            match instruction:
                case "do()":
                    multiplication_enabled = True
                case "don't()":
                    multiplication_enabled = False
                case _:
                    total += multiply(instruction) if multiplication_enabled else 0
    return total


def multiply(multiplication: str) -> int:
    operands: list[int] = [int(operand) for operand in re.findall("\d+", multiplication)]
    assert len(operands) == 2
    return operands[0] * operands[1]
