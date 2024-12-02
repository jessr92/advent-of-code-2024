from string_utils import string_to_list_ints


def part_1(reports: list[str]) -> int:
    return safe_report_count(reports)


def part_2(reports: list[str]) -> int:
    return safe_report_count(reports, True)


def safe_report_count(reports: list[str], allow_modification: bool = False) -> int:
    parsed_reports: list[list[int]] = [string_to_list_ints(report) for report in reports]
    return len([locations for locations in parsed_reports
                if is_safe(locations) or (allow_modification and safe_with_modification(locations))])


def safe_with_modification(locations: list[int]) -> bool:
    for i in range(len(locations)):
        if is_safe(locations[:i] + locations[i + 1:]):
            return True
    return False


def is_safe(locations: list[int]) -> bool:
    changes = [y - x for x, y in zip(locations, locations[1:])]
    must_increase = changes[0] > 0
    for change in changes:
        if bad_change(change, must_increase):
            return False
    return True


def bad_change(change: int, must_increase: bool) -> bool:
    if must_increase and change < 0:
        return True  # decrease but needs to increase
    elif not must_increase and change > 0:
        return True  # increase but needs to decrease
    elif change == 0:
        return True  # needs to change level
    elif abs(change) > 3:
        return True  # changing too quickly
    else:
        return False
