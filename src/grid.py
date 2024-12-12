from typing import Callable

from coord import Coord


class Grid[T]:
    _grid: list[list[T]]
    max_x: int
    max_y: int

    def __init__(self, raw_input: list[str], map_elements: Callable[[str], T] = lambda elem: elem):
        self._grid = []
        self.max_x = len(raw_input[0])
        self.max_y = len(raw_input)
        for y in range(self.max_y):
            self._grid.append([])
            for x in range(self.max_x):
                self._grid[y].append(map_elements(raw_input[y][x]))


    def inside_map(self, coord: Coord):
        return 0 <= coord.x < self.max_x and 0 <= coord.y < self.max_y

    def value_at(self, coord: Coord) -> T:
        return self._grid[coord.y][coord.x]

    def update_grid_at(self, coord: Coord, value: T):
        self._grid[coord.y][coord.x] = value
