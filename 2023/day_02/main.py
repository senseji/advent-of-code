from typing import List
from os import linesep

RED_MAX = 12
GREEEN_MAX = 13
BLUE_MAX = 14


class GameSet:
    red = 0
    green = 0
    blue = 0

    def __init__(self, input_string):
        split_to_colors = input_string.split(",")

        for cube_set in split_to_colors:
            for color in ["red", "green", "blue"]:
                if color in cube_set:
                    value = int(cube_set.replace(color, ""))
                    setattr(self, color, int(value))

    def is_valid(self):
        red_valid = self.red <= RED_MAX
        green_valid = self.green <= GREEEN_MAX
        blue_valid = self.blue <= BLUE_MAX
        return all([red_valid, green_valid, blue_valid])


class Game:
    id: int
    game_sets: List[GameSet]

    @staticmethod
    def get_id(_str: str):
        index = _str.rfind(" ")
        return int(_str[index::])

    def __init__(self, input_string):
        self.game_sets = []
        try:
            id_string, games = input_string.split(":")
        except Exception as e:
            print("INPUT STGRNG", input_string)
            raise e
        self.id = Game.get_id(id_string)

        split_games = games.split(";")
        for game in split_games:
            self.game_sets.append(GameSet(game))

    def __str__(self):
        print(f"GAME ", self.id)
        for game_set in self.game_sets:
            print(game_set.blue, game_set.red, game_set.green)

    def is_valid(self):
        if not self.game_sets:
            return False
        game_sets_valid = all([game_set.is_valid() for game_set in self.game_sets])
        print(f"Game {self.id} Valid? ", game_sets_valid)
        return game_sets_valid

    def get_power(self):
        power = 1
        for color in ["red", "green", "blue"]:
            power *= max([getattr(game_set, color) for game_set in self.game_sets])
        return power


def get_games_from_file():
    file_name = "input.txt"

    with open("input.txt", "r") as file:
        lines = file.readlines()

    games = []
    for line in lines:
        if line is linesep:
            continue
        games.append(Game(line))
    return games


def part_one():
    games = get_games_from_file()

    valid_games = [game for game in games if game.is_valid()]

    print(sum([game.id for game in valid_games]))


def part_two():
    games = get_games_from_file()

    powers = []
    for game in games:
        powers.append(game.get_power())

    print(sum(powers))


if __name__ == "__main__":
    part_one()
    part_two()
