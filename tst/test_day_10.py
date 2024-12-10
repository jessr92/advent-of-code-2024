import src.day10 as day10
from utils import read_all_of_file


def test_part_1_example():
    puzzle_input: list[str] = read_all_of_file("day_10_sample.txt")
    assert day10.part_1(puzzle_input) == 36


def test_part_1():
    puzzle_input: list[str] = read_all_of_file("day_10.txt")
    assert day10.part_1(puzzle_input) == 552


def test_part_2_examples():
    puzzle_input: list[str] = read_all_of_file("day_10_sample.txt")
    assert day10.part_2(puzzle_input) == 81


def test_part_2():
    puzzle_input: list[str] = read_all_of_file("day_10.txt")
    assert day10.part_2(puzzle_input) == 1225
