from collections import defaultdict
from itertools import combinations

from coord import Coord


def part_1(antennae_map: list[str]) -> int:
    antennae = extract_antenna_locations(antennae_map)
    max_x: int = len(antennae_map[0])
    max_y: int = len(antennae_map[1])

    antinodes: set[Coord] = set()
    for locations in antennae.values():
        for coord_pair in combinations(locations, 2):
            antinodes |= generate_antinodes(coord_pair[0], coord_pair[1], max_x, max_y)
    return len(antinodes)


def part_2(antennae_map: list[str]) -> int:
    antennae = extract_antenna_locations(antennae_map)
    max_x: int = len(antennae_map[0])
    max_y: int = len(antennae_map[1])

    antinodes: set[Coord] = set()
    for locations in antennae.values():
        for coord_pair in combinations(locations, 2):
            antinodes |= generate_all_antinodes(coord_pair[0], coord_pair[1], max_x, max_y)
    return len(antinodes)


def extract_antenna_locations(antennae_map):
    antennae: dict[str: set[Coord]] = defaultdict(set)
    for x in range(len(antennae_map[0])):
        for y in range(len(antennae_map)):
            coord: Coord = Coord(x, y)
            identifier: str = antennae_map[y][x]
            if identifier.isalnum():
                antennae[identifier].add(coord)
    return antennae


def generate_antinodes(a: Coord, b: Coord, max_x: int, max_y: int) -> set[Coord]:
    dx = b.x - a.x
    dy = b.y - a.y
    antinode1 = Coord(a.x - dx, a.y - dy)
    antinode2 = Coord(b.x + dx, b.y + dy)

    antinodes = set()
    if antinode1.inside_map(max_x, max_y):
        antinodes.add(antinode1)
    if antinode2.inside_map(max_x, max_y):
        antinodes.add(antinode2)
    return antinodes


def generate_all_antinodes(a: Coord, b: Coord, max_x: int, max_y: int) -> set[Coord]:
    antinodes = set()
    for x in range(max_x):
        for y in range(max_y):
            # if area of triangle defined by three coords is 0, they are in a line
            if a.x * (b.y - y) + b.x * (y - a.y) + x * (a.y - b.y) == 0:
                antinodes.add(Coord(x, y))
    return antinodes
