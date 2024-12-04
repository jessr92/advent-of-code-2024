import src.day4 as day4
from utils import read_all_of_file


def test_part_1_example():
    instructions: list[str] = read_all_of_file("day_4_sample.txt")
    assert day4.part_1(instructions) == 18


def test_part_1():
    instructions: list[str] = read_all_of_file("day_4.txt")
    assert day4.part_1(instructions) == 2603


def test_part_2_examples():
    instructions: list[str] = read_all_of_file("day_4_sample.txt")
    assert day4.part_2(instructions) == 9


def test_part_2():
    instructions: list[str] = read_all_of_file("day_4.txt")
    assert day4.part_2(instructions) == 1965
