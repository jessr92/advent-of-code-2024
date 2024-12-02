import src.day2 as day2
from utils import read_all_of_file


def test_part_1_example():
    locations = read_all_of_file("day_2_sample.txt")
    assert day2.part_1(locations) == 2


def test_part_1():
    locations = read_all_of_file("day_2.txt")
    assert day2.part_1(locations) == 383


def test_part_2_examples():
    locations = read_all_of_file("day_2_sample.txt")
    assert day2.part_2(locations) == 4


def test_part_2():
    locations = read_all_of_file("day_2.txt")
    assert day2.part_2(locations) == 436
