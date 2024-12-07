import src.day7 as day7
from utils import read_all_of_file


def test_part_1_example():
    instructions: list[str] = read_all_of_file("day_7_sample.txt")
    assert day7.part_1(instructions) == 3749


def test_part_1():
    instructions: list[str] = read_all_of_file("day_7.txt")
    assert day7.part_1(instructions) == 3245122495150


def test_part_2_examples():
    instructions: list[str] = read_all_of_file("day_7_sample.txt")
    assert day7.part_2(instructions) == 11387


def test_part_2():
    instructions: list[str] = read_all_of_file("day_7.txt")
    assert day7.part_2(instructions) == 105517128211543
