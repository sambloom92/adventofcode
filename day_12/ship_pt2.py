import os
from math import cos, radians, sin
from typing import Sequence

from conf import ROOT_DIR
from day_12.utils import Ship, get_instructions

INSTRUCTIONS_PATH = os.path.join(ROOT_DIR, "day_12/instructions.csv")
INSTRUCTIONS = get_instructions(INSTRUCTIONS_PATH)


class ShipPart2(Ship):
    def __init__(self):
        """
        ShipPart2 extends Ship
        the waypoint vector is the position of the waypoint relative to the ship
        the ship starts at 0, 0 and the waypoint starts at -1, 10 relative to the ship
        """
        super().__init__()
        self.waypoint_vector = [-1, 10]

    def translate_waypoint(self, vector: Sequence[float], n_steps: int):
        """
        translate the relative position of the waypoint by a given unit vector a given number of times
        :param vector: unit vector
        :param n_steps: number of times to translate
        """
        for component in range(len(self.coordinates)):
            self.waypoint_vector[component] += vector[component] * n_steps

    def rotate_waypoint(self, direction: str, argument: int):
        """
        rotate the waypoint vector about the origin by a given angle in a given direction
        :param direction: 'R' or 'L'
        :param argument: angle in degrees
        """
        if direction == "R":
            angle = radians(argument)
        else:
            angle = -1 * radians(argument)
        y = self.waypoint_vector[0]
        x = self.waypoint_vector[1]
        self.waypoint_vector[0] = int(round(x * sin(angle) + y * cos(angle)))
        self.waypoint_vector[1] = int(round(x * cos(angle) - y * sin(angle)))

    def execute_instruction(self, command: str, argument: int):
        """
        execute a given instruction
        :param command: a letter representing what to do
        :param argument: an argument representing a quantity - either an angle or number of steps
        """
        heading_letter_to_vector_map = {
            "N": (-1, 0),
            "E": (0, 1),
            "S": (1, 0),
            "W": (0, -1),
        }
        if command == "F":
            self.translate(self.waypoint_vector, argument)
        elif command in heading_letter_to_vector_map.keys():
            vector = heading_letter_to_vector_map[command]
            self.translate_waypoint(vector, argument)
        else:
            self.rotate_waypoint(command, argument)


if __name__ == "__main__":
    ship = ShipPart2()
    ship.execute_all_instructions(INSTRUCTIONS)
    print(ship.get_manhattan_distance())
