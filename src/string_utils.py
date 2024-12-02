import re


def string_to_list_ints(string_of_digits: str) -> list[int]:
    return [int(digits) for digits in re.findall(r'\d+', string_of_digits)]
