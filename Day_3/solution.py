import os
import re
from dataclasses import dataclass
from typing import Dict, List, Tuple, Union


@dataclass
class Number:
    value: int
    array_index: int
    position_index: List[int]

    def is_part_number(self, schematic) -> bool:
        part_number_flag: bool = False

        surround_elements = self.__get_surrounding_elements(
            array_index=self.array_index,
            position_index=self.position_index,
            schematic=schematic,
        )

        for element in surround_elements:
            if self.__is_symbol(element[0]):
                part_number_flag = True

        return part_number_flag

    def gear_locations(self, schematic) -> Union[List[Tuple[int, int]], None]:
        surround_elements = self.__get_surrounding_elements(
            array_index=self.array_index,
            position_index=self.position_index,
            schematic=schematic,
        )
        found_locations = []
        for element in surround_elements:
            if self.__is_gear(element[0]):
                location_tuple = (element[1], element[2])
                if location_tuple not in found_locations:
                    found_locations.append(location_tuple)
        return found_locations

    def __is_gear(self, char) -> bool:
        return char == "*"

    def __is_symbol(self, char: str) -> bool:
        return char != "." and not char.isdigit()

    def __get_surrounding_elements(
        self, array_index, position_index, schematic
    ) -> List[Tuple[str, int, int]]:
        num_rows, num_cols = len(schematic), len(schematic[0])
        result = []
        x = array_index
        for char_index in position_index:
            y = char_index
            for i in range(
                (0 if x - 1 < 0 else x - 1),
                (num_rows if x + 2 > num_rows else x + 2),
                1,
            ):
                for j in range(
                    (0 if y - 1 < 0 else y - 1),
                    (num_cols if y + 2 > num_cols else y + 2),
                    1,
                ):
                    if schematic[x][y] != schematic[i][j]:
                        result.append((schematic[i][j], i, j))
        return result


@dataclass
class Numbers:
    list_number: List[Number]


def read_input(filename: str) -> List[str]:
    """Reads input from a text file."""

    with open(file=filename, encoding="utf-8") as f:
        input_list = [line.rstrip() for line in f]
    return input_list


def build_numbers_object(input_str_list: List[str]) -> Numbers:
    number_obj_list: List[Number] = []
    for array_index, string_list in enumerate(input_str_list):
        string_numbers: List[str] = re.findall("[0-9]+", string_list)
        for string_number in string_numbers:
            match: Union[re.Match[str], None] = re.search(
                string_number, string_list
            )
            if not match:
                return Numbers(
                    list_number=[
                        Number(value=0, array_index=0, position_index=[0])
                    ]
                )
            index_tuple = match.span()
            string_list = string_list.replace(
                string_number, "." * len(string_number), 1
            )
            number_obj_list.append(
                build_number_object(
                    value=int(string_number),
                    array_index=array_index,
                    position_index=list(
                        range(index_tuple[0], index_tuple[1], 1)
                    ),
                )
            )

    return Numbers(list_number=number_obj_list)


def build_number_object(
    value: int, array_index: int, position_index: List[int]
) -> Number:
    number_object: Number = Number(
        value=value, array_index=array_index, position_index=position_index
    )
    return number_object


def part_one() -> None:
    """Calculates the results of Day 3 Part 1."""

    current_working_directory: str = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    schematic: List[str] = read_input(
        filename=current_working_directory + "/input.txt"
    )

    numbers_objects: Numbers = build_numbers_object(input_str_list=schematic)

    part_numbers = [
        number_object.value
        for number_object in numbers_objects.list_number
        if number_object.is_part_number(schematic=schematic)
    ]

    sum_part_numbers = sum(part_numbers)

    print(
        "Day 3 - Part 1 - The sum of all of the part numbers is:",
        sum_part_numbers,
    )


def part_two() -> None:
    """Calculates the results of Day 3 Part 2."""

    current_working_directory: str = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    schematic: List[str] = read_input(
        filename=current_working_directory + "/input.txt"
    )

    numbers_objects: Numbers = build_numbers_object(input_str_list=schematic)

    gear_location_to_value_map: Dict[Tuple[int, int], List[int]] = {}

    gear_part_numbers = [
        (
            number_object.gear_locations(schematic=schematic),
            number_object.value,
        )
        for number_object in numbers_objects.list_number
        if number_object.is_part_number(schematic=schematic)
        and number_object.gear_locations(schematic=schematic)
    ]

    for k, v in gear_part_numbers:
        if k is not None:
            for k_i in k:
                if k_i not in gear_location_to_value_map.keys():
                    gear_location_to_value_map[k_i] = [v]
                else:
                    gear_location_to_value_map[k_i].append(v)

    gear_ratio = [
        value[0] * value[1]
        for value in gear_location_to_value_map.values()
        if len(value) == 2
    ]

    sum_gear_ratio = sum(gear_ratio)

    print(
        "Day 3 - Part 2 - The sum of all of the gear part numbers is:",
        sum_gear_ratio,
    )


def main() -> None:
    """Main function"""

    part_one()
    part_two()


if __name__ == "__main__":
    main()
