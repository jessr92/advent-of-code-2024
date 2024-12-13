from collections import namedtuple

from coord import Coord
from string_utils import string_to_list_ints

Machine = namedtuple("Machine", ["button_a", "button_b", "prize"])
Solution = namedtuple("Solution", ["a_press_count", "b_press_count"])


def part_1(puzzle_input: list[str]) -> int:
    machines: list[Machine] = parse_input(puzzle_input)
    tokens: list[int] = [solution_cost(machine) for machine in machines]
    return sum(tokens)


def part_2(puzzle_input: list[str]) -> int:
    machines: list[Machine] = parse_input(puzzle_input, True)
    tokens: list[int] = [solution_cost(machine, True) for machine in machines]
    return sum(tokens)


def cost(solution: Solution) -> int:
    return (3 * solution.a_press_count) + solution.b_press_count


def solution_cost(machine: Machine, is_part_2: bool = False) -> int:
    # Cramer's rule for 2x2 systems with an integer check to find the valid solution
    a1: int = machine.button_a.x
    b1: int = machine.button_b.x
    c1: int = machine.prize.x

    a2: int = machine.button_a.y
    b2: int = machine.button_b.y
    c2: int = machine.prize.y

    coeff_mat_det = (a1 * b2) - (a2 * b1)
    x_numerator_det = (c1 * b2) - (c2 * b1)
    y_numerator_det = (a1 * c2) - (a2 * c1)

    if x_numerator_det % coeff_mat_det != 0 or y_numerator_det % coeff_mat_det != 0:
        return 0  # No integer solution

    a_press_count = int(x_numerator_det / coeff_mat_det)
    b_press_count = int(y_numerator_det / coeff_mat_det)

    if not is_part_2 and (a_press_count > 100 or b_press_count > 100):
        return 0  # Too many button presses

    return (3 * a_press_count) + b_press_count


def parse_input(puzzle_input: list[str], is_part_2: bool = False) -> list[Machine]:
    machines: list[Machine] = []
    button_a: Coord = Coord(0, 0)
    button_b: Coord = Coord(0, 0)
    correction: int = 10000000000000 if is_part_2 else 0
    for line in puzzle_input:
        number_list: list[int] = string_to_list_ints(line)
        if "Button A" in line:
            button_a = Coord(number_list[0], number_list[1])
        elif "Button B" in line:
            button_b = Coord(number_list[0], number_list[1])
        elif "Prize" in line:
            prize = Coord(number_list[0] + correction, number_list[1] + correction)
            machines.append(Machine(button_a, button_b, prize))
    return machines
