import os
from typing import Dict, List, Tuple

from conf import ROOT_DIR

INSTRUCTIONS_PATH = os.path.join(ROOT_DIR, "day_12/instructions.csv")


def get_instructions(filepath: str = INSTRUCTIONS_PATH) -> List[Dict[str, int]]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents
    :param filepath: path to file
    :return: list of instructions as strings
    """
    with open(filepath) as file:
        return [{line[0]: int(line[1:].strip())} for line in file.readlines()]


class Ship:
    def __init__(self):
        self.coordinates = [0, 0]
        self.heading = 90

    def change_heading(self, direction: str, angle: int):
        if direction == "R":
            angle_direction = 1
        else:
            angle_direction = -1
        self.heading = (self.heading + angle_direction * angle) % 360

    def translate(self, vector: Tuple[int, int], n_steps: int):
        for component in range(len(self.coordinates)):
            self.coordinates[component] += vector[component] * n_steps

    def execute_instruction(self, command: str, argument: int):
        heading_angle_to_vector_map = {
            0: (-1, 0),
            90: (0, 1),
            180: (+1, 0),
            270: (0, -1),
        }
        heading_letter_to_vector_map = {
            "N": (-1, 0),
            "E": (0, 1),
            "S": (+1, 0),
            "W": (0, -1),
        }
        if command == "F":
            vector = heading_angle_to_vector_map[self.heading]
            self.translate(vector, argument)
        elif command in heading_letter_to_vector_map.keys():
            vector = heading_letter_to_vector_map[command]
            self.translate(vector, argument)
        else:
            self.change_heading(command, argument)

    def get_manhattan_distance(self):
        return sum([abs(value) for value in self.coordinates])

    def execute_all_instructions(self, instructions: List[Dict[str, int]]):
        for instruction in instructions:
            command, argument = zip(*instruction.items())
            self.execute_instruction(*command, *argument)
