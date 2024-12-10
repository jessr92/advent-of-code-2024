from collections import namedtuple

from coord import Coord, UP, DOWN, LEFT, RIGHT

Visit = namedtuple("Visit", ["coord", "direction"])


class CycleDetected(Exception):
    def __init__(self, message):
        self.message = message


def part_1(guard_map: list[str]) -> int:
    current_position, direction = get_starting_position(guard_map)
    visited: set[Visit] = travel_through_guard_map(guard_map, current_position, direction)
    return len({visit.coord for visit in visited})


def part_2(guard_map: list[str]) -> int:
    current_position, direction = get_starting_position(guard_map)
    visited: set[Visit] = travel_through_guard_map(guard_map, current_position, direction)
    obstacle_candidates: set[Coord] = {visit.coord for visit in visited if visit.coord != current_position}
    obstacle_choices: int = 0
    for obstacle in obstacle_candidates:
        new_guard_map: list[str] = guard_map[:]
        row_to_update = new_guard_map[obstacle.y]
        new_guard_map[obstacle.y] = row_to_update[:obstacle.x] + '#' + row_to_update[obstacle.x + 1:]
        try:
            travel_through_guard_map(new_guard_map, current_position, direction)
        except CycleDetected:
            obstacle_choices += 1
    return obstacle_choices


def travel_through_guard_map(guard_map: list[str], current_position: Coord, direction: Coord) -> set[Visit]:
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


def inside_guard_map(guard_map: list[str], current_position: Coord, direction: Coord) -> bool:
    return current_position.move(direction).inside_map(len(guard_map[0]), len(guard_map))


def can_move(guard_map: list[str], current_position: Coord, direction: Coord) -> bool:
    new_position: Coord = current_position.move(direction)
    return guard_map[new_position.y][new_position.x] != "#"


def get_starting_position(guard_map: list[str]) -> (Coord, Coord):
    for x in range(len(guard_map[0])):
        for y in range(len(guard_map)):
            if guard_map[y][x] == "^":
                return Coord(x, y), UP
            elif [guard_map[y][x]] == ">":
                return Coord(x, y), RIGHT
            elif [guard_map[y][x]] == "<":
                return Coord(x, y), LEFT
            elif [guard_map[y][x]] == "v":
                return Coord(x, y), DOWN
    raise Exception("Could not find guard")
