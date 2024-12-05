from collections import defaultdict
from functools import cmp_to_key

from string_utils import string_to_list_ints


def part_1(page_numbers: list[str]) -> int:
    orderings, updates = parse_input(page_numbers)
    return sum([update[len(update) // 2] for update in updates if is_correctly_ordered(update, orderings)])


def part_2(page_numbers: list[str]) -> int:
    orderings, updates = parse_input(page_numbers)
    fixed_updates = [fix_update(update, orderings) for update in updates if not is_correctly_ordered(update, orderings)]
    return sum([update[len(update) // 2] for update in fixed_updates])


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


def fix_update(update: list[int], orderings: dict[int, set[int]]) -> list[int]:
    # if left page needs to be after right page in orderings, return 1 in comparator else return -1
    return sorted(update, key=cmp_to_key(lambda left, right: 1 if left in orderings[right] else -1))


def is_correctly_ordered(update: list[int], orderings: dict[int, set[int]]) -> bool:
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[i] in orderings[update[j]]:
                return False # page pair needs to be in opposite order
    return True
