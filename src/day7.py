from string_utils import string_to_list_ints


def part_1(equation_texts: list[str]) -> int:
    equations: list[list[int]] = [string_to_list_ints(equation_text) for equation_text in equation_texts]
    return sum([equation[0] for equation in equations if equation_solvable(equation)])


def part_2(equation_texts: list[str]) -> int:
    equations: list[list[int]] = [string_to_list_ints(equation_text) for equation_text in equation_texts]
    return sum([equation[0] for equation in equations if equation_solvable(equation, True)])


def equation_solvable(equation: list[int], include_concatenation: bool = False) -> bool:
    result: int = equation[0]
    first_operand: int = equation[1]
    other_operands: list[int] = equation[2:]
    return solution_exists(result, first_operand, other_operands, include_concatenation)


def solution_exists(result: int, left_operand: int, other_operands: list[int], include_concatenation: bool) -> bool:
    if len(other_operands) == 0:
        return result == left_operand
    if left_operand > result:
        return False
    right_operand = other_operands[0]
    remainder = other_operands[1:]
    addition: bool = solution_exists(result, left_operand + right_operand, remainder, include_concatenation)
    multiplication: bool = solution_exists(result, left_operand * right_operand, remainder, include_concatenation)
    concatenation: bool = solution_exists(result, int(f"{left_operand}{right_operand}"), remainder,
                                          include_concatenation) if include_concatenation else False
    return addition or multiplication or concatenation
