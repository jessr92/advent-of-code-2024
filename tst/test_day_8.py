import src.day8 as day8
from utils import read_all_of_file


def test_part_1_example():
    instructions: list[str] = read_all_of_file("day_8_sample.txt")
    assert day8.part_1(instructions) == 14


def test_part_1():
    instructions: list[str] = read_all_of_file("day_8.txt")
    assert day8.part_1(instructions) == 214


def test_part_2_examples():
    instructions: list[str] = read_all_of_file("day_8_sample.txt")
    assert day8.part_2(instructions) == 34


def test_part_2():
    instructions: list[str] = read_all_of_file("day_8.txt")
    assert day8.part_2(instructions) == 809
