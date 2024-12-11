import src.day11 as day11
from utils import read_all_of_file


def test_part_1_example():
    puzzle_input: list[str] = read_all_of_file("day_11_sample.txt")
    assert day11.part_1(puzzle_input) == 55312


def test_part_1():
    puzzle_input: list[str] = read_all_of_file("day_11.txt")
    assert day11.part_1(puzzle_input) == 186996


def test_part_2_examples():
    puzzle_input: list[str] = read_all_of_file("day_11_sample.txt")
    assert day11.part_2(puzzle_input) == 65601038650482


def test_part_2():
    puzzle_input: list[str] = read_all_of_file("day_11.txt")
    assert day11.part_2(puzzle_input) == 221683913164898
