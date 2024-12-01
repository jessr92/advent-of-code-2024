import bisect
import re
from collections import Counter


def part_1(locations: list[str]) -> int:
    left_locations, right_locations = extract_sorted_locations(locations)
    distance: int = 0
    for i in range(len(left_locations)):
        distance = distance + abs(left_locations[i] - right_locations[i])
    return distance


def part_2(locations: list[str]) -> int:
    left_locations, right_locations = extract_sorted_locations(locations)
    location_occurrences: dict[int, int] = Counter(right_locations)
    similarity: int = 0
    for location in left_locations:
        similarity = similarity + (location * location_occurrences[location])
    return similarity


def extract_sorted_locations(locations):
    left_locations: list[int] = []
    right_locations: list[int] = []
    for location in locations:
        extracted_locations = re.findall(r'\d+', location)
        assert len(extracted_locations) == 2
        bisect.insort(left_locations, int(extracted_locations[0]))
        bisect.insort(right_locations, int(extracted_locations[1]))
    return left_locations, right_locations
