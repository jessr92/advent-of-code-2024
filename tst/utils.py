def read_all_of_file(filename: str) -> list[str]:
    with open(filename, "r") as input:
        return input.readlines()
