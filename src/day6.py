type Coord = (int, int)
type Direction = (int, int)
type Visit = (Coord, Direction)

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)


class CycleDetected(Exception):
    def __init__(self, message):
        self.message = message


def part_1(map: list[str]) -> int:
    visited: set[Visit] = travel_through_map(map)
    return len({visit[0] for visit in visited})


def part_2(map: list[str]) -> int:
    current_position, _ = get_starting_position(map)
    visited: set[Coord] = travel_through_map(map)
    obstacle_candidates: set[Coord] = {visit[0] for visit in visited if visit[0] != current_position}
    obstacle_choices: int = 0
    for obstacle in obstacle_candidates:
        new_map: list[str] = map[:]
        row_to_update = new_map[obstacle[1]]
        new_map[obstacle[1]] = row_to_update[:obstacle[0]] + '#' + row_to_update[obstacle[0] + 1:]
        try:
            travel_through_map(new_map)
        except CycleDetected:
            obstacle_choices += 1
    return obstacle_choices


def travel_through_map(map: list[str]) -> set[Visit]:
    current_position, direction = get_starting_position(map)
    visited: set[Visit] = set()
    visited.add((current_position, direction))
    while not out_of_map(map, current_position, direction):
        while not can_move(map, current_position, direction):
            direction = turn_right(direction)
        current_position = move(current_position, direction)
        if (current_position, direction) in visited:
            raise CycleDetected(f"Cycle detected at {current_position}")
        visited.add((current_position, direction))
    return visited


def turn_right(direction: Direction) -> Direction:
    if direction == UP:
        return RIGHT
    elif direction == RIGHT:
        return DOWN
    elif direction == DOWN:
        return LEFT
    else:
        return UP


def out_of_map(map: list[str], current_position: Coord, direction: Direction) -> bool:
    maybe_new_position: Coord = move(current_position, direction)
    return maybe_new_position[0] < 0 or maybe_new_position[1] < 0 or \
        maybe_new_position[0] >= len(map[0]) or maybe_new_position[1] >= len(map)


def can_move(map: list[str], current_position: Coord, direction: Direction) -> bool:
    new_position: Coord = move(current_position, direction)
    return map[new_position[1]][new_position[0]] != "#"


def move(current_position: Coord, direction: Coord) -> Coord:
    return current_position[0] + direction[0], current_position[1] + direction[1]


def get_starting_position(map: list[str]) -> (Coord, Coord):
    x: int = 0
    y: int = 0
    for x in range(len(map[0])):
        for y in range(len(map)):
            if map[y][x] == "^":
                return (x, y), UP
            elif [map[y][x]] == ">":
                return (x, y), RIGHT
            elif [map[y][x]] == "<":
                return (x, y), LEFT
            elif [map[y][x]] == "v":
                return (x, y), DOWN
    raise Exception("Could not find guard")
