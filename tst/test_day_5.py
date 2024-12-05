import src.day5 as day5
from utils import read_all_of_file


def test_part_1_example():
    instructions: list[str] = read_all_of_file("day_5_sample.txt")
    assert day5.part_1(instructions) == 143


def test_part_1():
    instructions: list[str] = read_all_of_file("day_5.txt")
    assert day5.part_1(instructions) == 5268


def test_part_2_examples():
    instructions: list[str] = read_all_of_file("day_5_sample.txt")
    assert day5.part_2(instructions) == 123


def test_part_2():
    instructions: list[str] = read_all_of_file("day_5.txt")
    assert day5.part_2(instructions) == 5799
