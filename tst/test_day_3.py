import src.day3 as day3
from utils import read_all_of_file


def test_part_1_example():
    instructions: list[str] = read_all_of_file("day_3_part_1_sample.txt")
    assert day3.part_1(instructions) == 161


def test_part_1():
    instructions: list[str] = read_all_of_file("day_3.txt")
    assert day3.part_1(instructions) == 173731097


def test_part_2_examples():
    instructions: list[str] = read_all_of_file("day_3_part_2_sample.txt")
    assert day3.part_2(instructions) == 48


def test_part_2():
    instructions: list[str] = read_all_of_file("day_3.txt")
    assert day3.part_2(instructions) == 93729253
