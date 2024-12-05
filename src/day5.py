from collections import defaultdict
from functools import cmp_to_key

from string_utils import string_to_list_ints


def part_1(page_numbers: list[str]) -> int:
    orderings, updates = parse_input(page_numbers)
    return sum([update[len(update) // 2] for update in updates
                if update == fix_update(update, orderings)])


def part_2(page_numbers: list[str]) -> int:
    orderings, updates = parse_input(page_numbers)
    return sum([fixed_update[len(fixed_update) // 2] for update in updates
                if update != (fixed_update := fix_update(update, orderings))])


def fix_update(update: list[int], orderings: dict[int, set[int]]) -> list[int]:
    # if left page needs to be after right page in orderings, return 1 in comparator else return -1
    return sorted(update, key=cmp_to_key(lambda left, right: 1 if left in orderings[right] else -1))


def parse_input(page_numbers: list[str]):
    orderings: dict[int, set[int]] = defaultdict(set)
    updates: list[list[int]] = []
    completed_orderings = False
    for i in range(len(page_numbers)):
        if not page_numbers[i]:
            completed_orderings = True
        elif completed_orderings:
            updates.append(string_to_list_ints(page_numbers[i]))
        else:
            page_pair: list[str] = page_numbers[i].split("|")
            orderings[int(page_pair[0])].add(int(page_pair[1]))
    return orderings, updates
