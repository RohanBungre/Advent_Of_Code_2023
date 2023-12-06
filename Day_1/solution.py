import os
from typing import Dict, List


def read_input(filename: str) -> List[str]:
    """Reads input from a text file."""

    with open(file=filename, encoding="utf-8") as f:
        input_list = [line.rstrip() for line in f]
    return input_list


def convert_spelled_number_to_char(input_list: List[str]) -> List[str]:
    """Converts a spelled out number into its character representation."""

    output_list: List[str] = []
    spelling_to_number_map: Dict[str, str] = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5r",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    for string in input_list:
        converted_string = string
        for spelling_key, number_value in spelling_to_number_map.items():
            if spelling_key in converted_string:
                converted_string = converted_string.replace(
                    spelling_key, number_value
                )
        output_list.append(converted_string)
    return output_list


def remove_non_digit_chars(input_list: List[str]) -> List[str]:
    """Removes all non digit characters from a list of strings."""

    output_list: List[str] = []
    for string in input_list:
        output_list.append("".join(char for char in string if char.isdigit()))
    return output_list


def first_and_last_number(input_list: List[str]) -> List[int]:
    """Takes the first and last number and generates an interger value."""

    output_list: List[int] = []
    for string_number in input_list:
        integer_number: int = (
            int(string_number[0]) * 10 + int(string_number[-1]) * 1
        )
        output_list.append(integer_number)
    return output_list


def part_one() -> None:
    """Calculates the results of Day 1 Part 1."""

    current_working_directory: str = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    input_str_list: List[str] = read_input(
        filename=current_working_directory + "/input.txt"
    )

    number_str_list: List[str] = remove_non_digit_chars(
        input_list=input_str_list
    )

    number_int_list: List[int] = first_and_last_number(
        input_list=number_str_list
    )

    sum_of_number_int_list = sum(number_int_list)

    print(
        "Day 1 - Part 1 - The sum of all of the calibration values is:",
        sum_of_number_int_list,
    )


def part_two() -> None:
    """Calculates the results of Day 1 Part 2."""

    current_working_directory: str = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    input_str_list: List[str] = read_input(
        filename=current_working_directory + "/input.txt"
    )

    number_converted_str_list: List[str] = convert_spelled_number_to_char(
        input_list=input_str_list
    )

    number_str_list: List[str] = remove_non_digit_chars(
        input_list=number_converted_str_list
    )

    number_int_list: List[int] = first_and_last_number(
        input_list=number_str_list
    )

    sum_of_number_int_list = sum(number_int_list)

    print(
        "Day 1 - Part 2 - The sum of all of the calibration values is:",
        sum_of_number_int_list,
    )


def main() -> None:
    """Main function"""

    part_one()
    part_two()


if __name__ == "__main__":
    main()
