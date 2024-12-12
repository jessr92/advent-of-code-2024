class Coord:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, movement):
        return Coord(self.x + movement.x, self.y + movement.y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(repr(self))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"


UP: Coord = Coord(0, -1)
RIGHT: Coord = Coord(1, 0)
DOWN: Coord = Coord(0, 1)
LEFT: Coord = Coord(-1, 0)
UP_LEFT: Coord = Coord(-1, -1)
UP_RIGHT: Coord = Coord(1, -1)
DOWN_LEFT: Coord = Coord(-1, 1)
DOWN_RIGHT: Coord = Coord(1, 1)
