import bisect
import re
from collections import Counter
from functools import reduce


def part_1(locations: list[str]) -> int:
    left_locations, right_locations = extract_sorted_locations(locations)
    distances: list[int] = [abs(left - right) for left, right, in zip(left_locations, right_locations)]
    return sum(distances)


def part_2(locations: list[str]) -> int:
    left_locations, right_locations = extract_sorted_locations(locations)
    right_occurrences: dict[int, int] = Counter(right_locations)
    return reduce(lambda similarity, location: similarity + (location * right_occurrences[location]), left_locations, 0)


def extract_sorted_locations(locations):
    left_locations: list[int] = []
    right_locations: list[int] = []
    for location in locations:
        extracted_locations = re.findall(r'\d+', location)
        assert len(extracted_locations) == 2
        bisect.insort(left_locations, int(extracted_locations[0]))
        bisect.insort(right_locations, int(extracted_locations[1]))
    return left_locations, right_locations
