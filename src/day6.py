import copy
from collections import namedtuple

from coord import Coord, UP, DOWN, LEFT, RIGHT
from grid import Grid

Visit = namedtuple("Visit", ["coord", "direction"])


class CycleDetected(Exception):
    def __init__(self, message):
        self.message = message


def part_1(puzzle_input: list[str]) -> int:
    guard_map: Grid[str] = Grid(puzzle_input)
    current_position, direction = get_starting_position(guard_map)
    visited: set[Visit] = travel_through_guard_map(guard_map, current_position, direction)
    return len({visit.coord for visit in visited})


def part_2(puzzle_input: list[str]) -> int:
    guard_map: Grid[str] = Grid(puzzle_input)
    current_position, direction = get_starting_position(guard_map)
    visited: set[Visit] = travel_through_guard_map(guard_map, current_position, direction)
    obstacle_candidates: set[Coord] = {visit.coord for visit in visited if visit.coord != current_position}
    obstacle_choices: int = 0
    for obstacle in obstacle_candidates:
        new_guard_map: Grid[str] = copy.deepcopy(guard_map)
        new_guard_map.update_grid_at(obstacle, '#')
        try:
            travel_through_guard_map(new_guard_map, current_position, direction)
        except CycleDetected:
            obstacle_choices += 1
    return obstacle_choices


def travel_through_guard_map(guard_map: Grid[str], current_position: Coord, direction: Coord) -> set[Visit]:
    visited: set[Visit] = set()
    visited.add(Visit(current_position, direction))
    while inside_guard_map(guard_map, current_position, direction):
        while not can_move(guard_map, current_position, direction):
            direction = turn_right(direction)
        current_position = current_position.move(direction)
        if (current_position, direction) in visited:
            raise CycleDetected(f"Cycle detected at {current_position}")
        visited.add(Visit(current_position, direction))
    return visited


def turn_right(direction: Coord) -> Coord:
    if direction == UP:
        return RIGHT
    elif direction == RIGHT:
        return DOWN
    elif direction == DOWN:
        return LEFT
    else:
        return UP


def inside_guard_map(guard_map: Grid, current_position: Coord, direction: Coord) -> bool:
    return guard_map.inside_map(current_position.move(direction))


def can_move(guard_map: Grid[str], current_position: Coord, direction: Coord) -> bool:
    new_position: Coord = current_position.move(direction)
    return guard_map.value_at(new_position) != "#"


def get_starting_position(guard_map: Grid[str]) -> (Coord, Coord):
    for x in range(guard_map.max_x):
        for y in range(guard_map.max_y):
            coord: Coord = Coord(x, y)
            map_elem: str = guard_map.value_at(coord)
            if map_elem == "^":
                return Coord(x, y), UP
            elif map_elem == ">":
                return Coord(x, y), RIGHT
            elif map_elem == "<":
                return Coord(x, y), LEFT
            elif map_elem == "v":
                return Coord(x, y), DOWN
    raise Exception("Could not find guard")
