from typing import List


def read_input(filename: str) -> List[str]:
    """Reads input from a text file."""
    with open(file=filename, encoding="utf-8") as f:
        input_list = [line.rstrip() for line in f]
    return input_list
