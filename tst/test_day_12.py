import src.day12 as day12
from utils import read_all_of_file


def test_part_1_example_1():
    puzzle_input: list[str] = read_all_of_file("day_12_sample_1.txt")
    assert day12.part_1(puzzle_input) == 140


def test_part_1_example_2():
    puzzle_input: list[str] = read_all_of_file("day_12_sample_2.txt")
    assert day12.part_1(puzzle_input) == 772


def test_part_1_example_3():
    puzzle_input: list[str] = read_all_of_file("day_12_sample_3.txt")
    assert day12.part_1(puzzle_input) == 1930


def test_part_1():
    puzzle_input: list[str] = read_all_of_file("day_12.txt")
    assert day12.part_1(puzzle_input) == 1415378


def test_part_2_example_1():
    puzzle_input: list[str] = read_all_of_file("day_12_sample_1.txt")
    assert day12.part_2(puzzle_input) == 80


def test_part_2_example_2():
    puzzle_input: list[str] = read_all_of_file("day_12_sample_2.txt")
    assert day12.part_2(puzzle_input) == 436


def test_part_2_example_3():
    puzzle_input: list[str] = read_all_of_file("day_12_sample_3.txt")
    assert day12.part_2(puzzle_input) == 1206


def test_part_2_example_4():
    puzzle_input: list[str] = read_all_of_file("day_12_sample_4.txt")
    assert day12.part_2(puzzle_input) == 236


def test_part_2_example_5():
    puzzle_input: list[str] = read_all_of_file("day_12_sample_5.txt")
    assert day12.part_2(puzzle_input) == 368


def test_part_2():
    puzzle_input: list[str] = read_all_of_file("day_12.txt")
    assert day12.part_2(puzzle_input) == 862714
