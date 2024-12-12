from collections import defaultdict
from itertools import combinations

from coord import Coord
from grid import Grid


def part_1(puzzle_input: list[str]) -> int:
    antennae_map: Grid[str] = Grid(puzzle_input)
    antennae = extract_antenna_locations(antennae_map)

    antinodes: set[Coord] = set()
    for locations in antennae.values():
        for coord_pair in combinations(locations, 2):
            antinodes |= generate_antinodes(coord_pair[0], coord_pair[1], antennae_map)
    return len(antinodes)


def part_2(puzzle_input: list[str]) -> int:
    antennae_map: Grid[str] = Grid(puzzle_input)
    antennae = extract_antenna_locations(antennae_map)

    antinodes: set[Coord] = set()
    for locations in antennae.values():
        for coord_pair in combinations(locations, 2):
            antinodes |= generate_all_antinodes(coord_pair[0], coord_pair[1], antennae_map)
    return len(antinodes)


def extract_antenna_locations(antennae_map: Grid[str]):
    antennae: dict[str: set[Coord]] = defaultdict(set)
    for x in range(antennae_map.max_x):
        for y in range(antennae_map.max_y):
            coord: Coord = Coord(x, y)
            identifier: str = antennae_map.value_at(coord)
            if identifier.isalnum():
                antennae[identifier].add(coord)
    return antennae


def generate_antinodes(a: Coord, b: Coord, antennae_map: Grid[str]) -> set[Coord]:
    dx = b.x - a.x
    dy = b.y - a.y
    antinode1 = Coord(a.x - dx, a.y - dy)
    antinode2 = Coord(b.x + dx, b.y + dy)

    antinodes = set()
    if antennae_map.inside_map(antinode1):
        antinodes.add(antinode1)
    if antennae_map.inside_map(antinode2):
        antinodes.add(antinode2)
    return antinodes


def generate_all_antinodes(a: Coord, b: Coord, antenna_map: Grid[str]) -> set[Coord]:
    antinodes = set()
    for x in range(antenna_map.max_x):
        for y in range(antenna_map.max_y):
            # if area of triangle defined by three coords is 0, they are in a line
            if a.x * (b.y - y) + b.x * (y - a.y) + x * (a.y - b.y) == 0:
                antinodes.add(Coord(x, y))
    return antinodes
