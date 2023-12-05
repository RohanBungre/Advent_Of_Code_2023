import os
import re
from typing import List


def read_input(filename: str) -> List[str]:
    """Reads input from a text file."""
    with open(file=filename, encoding="utf-8") as f:
        input_list = [line.rstrip() for line in f]
    return input_list


def find_max_colour(input_string: str, colour: str) -> int:
    """Finds the max number of dice for a given colour."""
    pattern = rf"[0-9]+\s{colour}+"
    regex_pattern = re.compile(pattern=pattern, flags=re.IGNORECASE)
    match_strings = regex_pattern.findall(string=input_string)

    if len(match_strings) == 0:
        return 0

    number_int_list = []
    for match_string in match_strings:
        number_int_list.append(
            int("".join(char for char in match_string if char.isdigit()))
        )
    max_number = max(number_int_list)
    return max_number


def is_valid_game(
    input_string: str, no_red: int, no_green: int, no_blue: int
) -> bool:
    """Validates if a game is valid."""
    max_red = find_max_colour(input_string=input_string, colour="red")
    max_green = find_max_colour(input_string=input_string, colour="green")
    max_blue = find_max_colour(input_string=input_string, colour="blue")
    if max_red > no_red or max_green > no_green or max_blue > no_blue:
        print(
            input_string,
            max_red > no_red,
            max_green > no_green,
            max_blue > no_blue,
        )
        return False
    else:
        return True


def part_one() -> None:
    """Calculates the results of Day 2 Part 1."""
    current_working_directory: str = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    input_str_list: List[str] = read_input(
        filename=current_working_directory + "/input.txt"
    )

    valid_id_list = []

    for index, input_string in enumerate(input_str_list):
        if is_valid_game(
            input_string=input_string, no_red=12, no_green=13, no_blue=14
        ):
            valid_id_list.append(index + 1)

    valid_id_list_sum = sum(valid_id_list)

    print(valid_id_list)
    print(valid_id_list_sum)


def main() -> None:
    """Main function"""
    part_one()


if __name__ == "__main__":
    main()
