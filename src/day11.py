from collections import namedtuple

from string_utils import string_to_list_ints

MemoryKey = namedtuple("MemoryKey", ["stone", "blinks"])
type MemoryValue = int

memory: dict[MemoryKey, MemoryValue] = {}


def part_1(puzzle_input: list[str]) -> int:
    stones: list[int] = string_to_list_ints(puzzle_input[0])
    iterations: int = 25
    blinked_stones: list[int] = [blink_stone_count(stone, iterations) for stone in stones]
    return sum(blinked_stones)


def part_2(puzzle_input: list[str]) -> int:
    stones: list[int] = string_to_list_ints(puzzle_input[0])
    iterations: int = 75
    blinked_stones: list[int] = [blink_stone_count(stone, iterations) for stone in stones]
    return sum(blinked_stones)


def blink_stone_count(stone: int, blinks: int) -> int:
    if blinks == 0:
        # Terminating case, stone count unchanged
        return 1
    elif MemoryKey(stone, blinks) in memory:
        # We've been here before so skip calculating
        return memory[MemoryKey(stone, blinks)]
    elif stone == 0:
        # 0-value stone replaced with 1-value stone
        value = blink_stone_count(1, blinks - 1)
    elif len(stone_str := str(stone)) % 2 == 0:
        # Even length stone value so we split it into two
        left_stone_half_count = blink_stone_count(int(stone_str[:len(stone_str) // 2]), blinks - 1)
        right_stone_half_count = blink_stone_count(int(stone_str[len(stone_str) // 2:]), blinks - 1)
        value = left_stone_half_count + right_stone_half_count
    else:
        # Fallback rule multiplies stone value by 2024
        value = blink_stone_count(stone * 2024, blinks - 1)
    memory[MemoryKey(stone, blinks)] = value
    return value
