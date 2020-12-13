import os
from abc import ABC, abstractmethod
from typing import Dict, List, Sequence

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


class Ship(ABC):
    def __init__(self):
        """
        the ship starts at 0, 0  and heading East (90 degrees)
        """
        self.coordinates = [0, 0]

    @abstractmethod
    def execute_instruction(self, command: str, argument: int):
        ...

    def translate(self, vector: Sequence[float], n_steps: int):
        """
        translate the ship's position by a given unit vector, a given number of times
        :param vector: a unit vector
        :param n_steps: how many times to translate
        """
        self.coordinates[0] += vector[0] * n_steps
        self.coordinates[1] += vector[1] * n_steps

    def get_manhattan_distance(self) -> int:
        """
        get the manhattan distance from 0, 0 to the current position
        :return: distance
        """
        return sum([abs(value) for value in self.coordinates])

    def execute_all_instructions(self, instructions: List[Dict[str, int]]):
        """
        execute a sequence of instructions
        :param instructions: sequence of instructions
        """
        for instruction in instructions:
            command, argument = zip(*instruction.items())
            self.execute_instruction(*command, *argument)
