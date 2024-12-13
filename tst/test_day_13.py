import src.day13 as day13
from utils import read_all_of_file


def test_part_1_example():
    puzzle_input: list[str] = read_all_of_file("day_13_sample.txt")
    assert day13.part_1(puzzle_input) == 480


def test_part_1():
    puzzle_input: list[str] = read_all_of_file("day_13.txt")
    assert day13.part_1(puzzle_input) == 30973


def test_part_2_examples():
    puzzle_input: list[str] = read_all_of_file("day_13_sample.txt")
    assert day13.part_2(puzzle_input) == 875318608908


def test_part_2():
    puzzle_input: list[str] = read_all_of_file("day_13.txt")
    assert day13.part_2(puzzle_input) == 95688837203288
