PART_1_TARGET: str = "XMAS"
PART_2_TARGET: str = "MAS"


def part_1(word_search: list[str]) -> int:
    return horizontal_matches(word_search) + vertical_matches(word_search) + diagonal_matches(word_search)


def part_2(word_search: list[str]) -> int:
    total: int = 0
    print()
    for x in range(len(word_search[0]) - 2):
        for y in range(len(word_search) - 2):
            south_east: str = word_search[y][x] + word_search[y+1][x+1] + word_search[y+2][x+2]
            north_east: str = word_search[y+2][x] + word_search[y+1][x+1] + word_search[y][x+2]
            south_west: str = word_search[y][x+2] + word_search[y+1][x+1] + word_search[y+2][x]
            north_west: str = word_search[y+2][x+2] + word_search[y+1][x+1] + word_search[y][x]
            if south_east == PART_2_TARGET and north_east == PART_2_TARGET:
                total += 1
            if north_west == PART_2_TARGET and north_east == PART_2_TARGET:
                total += 1
            if south_east == PART_2_TARGET and south_west == PART_2_TARGET:
                total += 1
            if north_west == PART_2_TARGET and south_west == PART_2_TARGET:
                total += 1
    return total


def horizontal_matches(word_search: list[str]) -> int:
    return sum([line.count(PART_1_TARGET) + line[::-1].count(PART_1_TARGET) for line in word_search])


def vertical_matches(word_search: list[str]) -> int:
    inverted: list[str] = []
    for char_num in range(len(word_search[0])):
        vertical: str = ""
        for line in word_search:
            vertical += line[char_num]
        inverted.append(vertical)
    return horizontal_matches(inverted)


def diagonal_matches(word_search: list[str]) -> int:
    forward_diagonals: list[str] = ["" for _ in range(len(word_search) * 2 - 1)]
    for x in range(len(word_search[0])):
        for y in range(len(word_search)):
            forward_diagonals[x + y] += word_search[y][x]
    forward_matches: int = horizontal_matches(forward_diagonals)

    backward_diagonals: list[str] = ["" for _ in range(len(word_search) * 2 - 1)]
    for x in range(len(word_search[0])):
        for y in range(len(word_search)):
            backward_diagonals[x - y] += word_search[y][x]
    backward_matches = horizontal_matches(backward_diagonals)
    return forward_matches + backward_matches
