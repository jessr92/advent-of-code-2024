import src.day9 as day9
from utils import read_all_of_file


def test_part_1_example():
    instructions: list[str] = read_all_of_file("day_9_sample.txt")
    assert day9.part_1(instructions) == 1928


def test_part_1():
    instructions: list[str] = read_all_of_file("day_9.txt")
    assert day9.part_1(instructions) == 6283170117911


def test_part_2_examples():
    instructions: list[str] = read_all_of_file("day_9_sample.txt")
    assert day9.part_2(instructions) == 2858


def test_part_2():
    instructions: list[str] = read_all_of_file("day_9.txt")
    assert day9.part_2(instructions) == 6307653242596
