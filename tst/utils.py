def read_all_of_file(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return [line.rstrip() for line in file.readlines()]
