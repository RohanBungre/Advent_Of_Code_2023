import os
import re
from dataclasses import dataclass
from typing import List


@dataclass
class Set:
    """Dataclass to store a Game's induvidual Set object."""

    red: int = 0
    green: int = 0
    blue: int = 0


@dataclass
class Game:
    """Dataclass to store a each Game object."""

    id: int
    set_list: List[Set]

    def max_red(self) -> int:
        return max([value.red for value in self.set_list])

    def max_green(self) -> int:
        return max([value.green for value in self.set_list])

    def max_blue(self) -> int:
        return max([value.blue for value in self.set_list])

    def is_valid(self, red_limit, green_limit, blue_limit) -> bool:
        if (
            self.max_red() > red_limit
            or self.max_green() > green_limit
            or self.max_blue() > blue_limit
        ):
            return False
        else:
            return True


@dataclass
class Games:
    """Dataclass to store a collection of Game objects."""

    game_list: List[Game]


def read_input(filename: str) -> List[str]:
    """Reads input from a text file."""
    with open(file=filename, encoding="utf-8") as f:
        input_list = [line.rstrip() for line in f]
    return input_list


def build_set_object(input_string) -> Set:
    red_number: int = find_number_for_colour(
        input_string=input_string, colour="red"
    )
    green_number: int = find_number_for_colour(
        input_string=input_string, colour="green"
    )
    blue_number: int = find_number_for_colour(
        input_string=input_string, colour="blue"
    )
    return Set(red=red_number, green=green_number, blue=blue_number)


def build_games_object(input_str_list: List[str]) -> Games:
    """Builds a Games object from the input data."""

    game_obj_list: List[Game] = []

    for input_game_str in input_str_list:
        colon_split = input_game_str.split(sep=":")
        game_id = int(colon_split[0].split(sep=" ")[-1])
        semi_colon_split = colon_split[1].split(";")
        set_obj_list: list[Set] = []

        for string in semi_colon_split:
            set_obj = build_set_object(string)
            set_obj_list.append(set_obj)

        game_obj = Game(id=game_id, set_list=set_obj_list)
        game_obj_list.append(game_obj)

    return Games(game_list=game_obj_list)


def find_number_for_colour(input_string: str, colour: str) -> int:
    """Finds the max number of dice for a given colour."""

    pattern: str = rf"[0-9]+\s{colour}+"
    regex_pattern: re.Pattern[str] = re.compile(
        pattern=pattern, flags=re.IGNORECASE
    )
    match_strings: List[str] = regex_pattern.findall(string=input_string)
    if len(match_strings) == 0:
        return 0
    else:
        match_string: str = match_strings[0]
    found_number: int = int(
        "".join(char for char in match_string if char.isdigit())
    )
    return found_number


def part_one() -> None:
    """Calculates the results of Day 2 Part 1."""

    current_working_directory: str = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    input_str_list: List[str] = read_input(
        filename=current_working_directory + "/input.txt"
    )

    games_obj: Games = build_games_object(input_str_list=input_str_list)

    valid_id_list: List[int] = [
        game_obj.id
        for game_obj in games_obj.game_list
        if game_obj.is_valid(red_limit=12, green_limit=13, blue_limit=14)
    ]

    valid_id_list_sum = sum(valid_id_list)

    print(
        "Day 2 - Part 1 - The sum of all of the valid ids is:",
        valid_id_list_sum,
    )


def part_two() -> None:
    """Calculates the results of Day 2 Part 2."""

    current_working_directory: str = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    input_str_list: List[str] = read_input(
        filename=current_working_directory + "/input.txt"
    )

    games_obj: Games = build_games_object(input_str_list=input_str_list)

    power_list: List[int] = [
        game_obj.max_red() * game_obj.max_green() * game_obj.max_blue()
        for game_obj in games_obj.game_list
    ]

    power_list_sum = sum(power_list)

    print(
        "Day 2 - Part 1 - The sum of all of the powers is:",
        power_list_sum,
    )


def main() -> None:
    """Main function"""

    part_one()
    part_two()


if __name__ == "__main__":
    main()
