import src.day6 as day6
from utils import read_all_of_file


def test_part_1_example():
    instructions: list[str] = read_all_of_file("day_6_sample.txt")
    assert day6.part_1(instructions) == 41


def test_part_1():
    instructions: list[str] = read_all_of_file("day_6.txt")
    assert day6.part_1(instructions) == 5269


def test_part_2_examples():
    instructions: list[str] = read_all_of_file("day_6_sample.txt")
    assert day6.part_2(instructions) == 6


def test_part_2():
    instructions: list[str] = read_all_of_file("day_6.txt")
    assert day6.part_2(instructions) == 1957
