import src.day1 as day1
from utils import read_all_of_file


def test_part_1_example():
    locations = read_all_of_file("day_1_sample.txt")
    assert day1.part_1(locations) == 11


def test_part_1():
    locations = read_all_of_file("day_1.txt")
    assert day1.part_1(locations) == 1765812


def test_part_2_examples():
    locations = read_all_of_file("day_1_sample.txt")
    assert day1.part_2(locations) == 31

def test_part_2():
    locations = read_all_of_file("day_1.txt")
    assert day1.part_2(locations) == 20520794
