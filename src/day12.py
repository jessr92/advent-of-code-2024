from collections import namedtuple

from coord import Coord, UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT

type Direction = Coord

CARDINAL_DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
DIAGONAL_DIRECTIONS = [UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]

GardenPlot = namedtuple("GardenPlot", ["coord", "plant"])


def part_1(puzzle_input: list[str]) -> int:
    regions = find_regions(puzzle_input)
    return sum([region_price(region) for region in regions])


def part_2(puzzle_input: list[str]) -> int:
    regions = find_regions(puzzle_input)
    return sum([discounted_region_price(region) for region in regions])


def find_regions(puzzle_input):
    max_x: int = len(puzzle_input[0])
    max_y: int = len(puzzle_input)
    regions: list[(str, set[Coord])] = []
    visited: set[Coord] = set()
    for y in range(max_y):
        for x in range(max_x):
            coord: Coord = Coord(x, y)
            plant: str = puzzle_input[y][x]
            if coord in visited:
                continue
            region = set(find_region(coord, puzzle_input, visited))
            for coord in region:
                visited.add(coord)
            if len(region) > 0:
                regions.append((plant, region))
    return regions


def find_region(coord: Coord, grid: list[str], visited: set[Coord]) -> list[Coord]:
    if coord in visited:
        return []
    visited.add(coord)
    region_coords: list[Coord] = [coord]
    max_x: int = len(grid[0])
    max_y: int = len(grid)

    for direction in CARDINAL_DIRECTIONS:
        next_coord = coord.move(direction)
        if not (0 <= next_coord.x < max_x and 0 <= next_coord.y < max_y):
            continue  # outside of grid
        if grid[next_coord.y][next_coord.x] != grid[coord.y][coord.x]:
            continue  # wrong plant
        flooded_coords = find_region(next_coord, grid, visited)
        region_coords += flooded_coords
    return region_coords


def get_cardinal_coords(coord: Coord) -> list[Coord]:
    return [coord.move(direction) for direction in CARDINAL_DIRECTIONS]


def region_price(region: (str, set[GardenPlot])) -> int:
    area: int = len(region[1])
    perimeter: int = region_perimeter(region[1])
    return area * perimeter


def discounted_region_price(region: (str, set[GardenPlot])) -> int:
    area: int = len(region[1])
    sides: int = region_sides(region[1])
    return area * sides


def region_perimeter(region: set[Coord]) -> int:
    perimeter: int = 0
    for coord in region:
        perimeter += 4  # Initially assume coord on its own
        for direction in CARDINAL_DIRECTIONS:
            adjacent_coord: Coord = coord.move(direction)
            if adjacent_coord in region:
                perimeter -= 1  # No perimeter fence as adjacent coord in region
    return perimeter


def region_sides(region: set[Coord]) -> int:
    sides: int = 0
    for coord in region:
        sides += corners_for(region, coord)  # Every corner adds a side
    return sides


def corners_for(region: set[Coord], coord: Coord) -> int:
    corners = 0
    up = coord.move(UP)
    down = coord.move(DOWN)
    left = coord.move(LEFT)
    right = coord.move(RIGHT)
    # A corner is present if
    # a) diagonal of two cardinal direction plots not present in region when those plots are present
    # b) Neither of those cardinal direction plot pairs are present, irrespective of the diagonal direction (the
    # diagonal would be part of another region regardless in that case)
    if up in region:
        up_left = coord.move(UP_LEFT)
        up_right = coord.move(UP_RIGHT)
        if left in region and up_left not in region:
            corners += 1
        if right in region and up_right not in region:
            corners += 1
    else:
        if left not in region:
            corners += 1
        if right not in region:
            corners += 1
    if down in region:
        down_left = coord.move(DOWN_LEFT)
        down_right = coord.move(DOWN_RIGHT)
        if left in region and down_left not in region:
            corners += 1
        if right in region and down_right not in region:
            corners += 1
    else:
        if left not in region:
            corners += 1
        if right not in region:
            corners += 1
    return corners
