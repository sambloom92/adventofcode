import os

from conf import ROOT_DIR
from day_12.utils import Ship, get_instructions

INSTRUCTIONS_PATH = os.path.join(ROOT_DIR, "day_12/instructions.csv")
INSTRUCTIONS = get_instructions(INSTRUCTIONS_PATH)


class ShipPart1(Ship):
    def __init__(self):
        """
        ShipPart1 extends Ship
        the ship starts at 0, 0  and heading East (90 degrees)
        """
        super().__init__()
        self.heading = 90

    def change_heading(self, direction: str, angle: int):
        """
        change the ship's heading by a given angle in a given direction
        :param direction: 'R' or 'L'
        :param angle: angle in degrees
        """
        if direction == "R":
            angle_direction = 1
        else:
            angle_direction = -1
        self.heading = (self.heading + angle_direction * angle) % 360

    def execute_instruction(self, command: str, argument: int):
        """
        execute a given instruction
        :param command: a letter representing what to do
        :param argument: an argument representing a quantity - either an angle or number of steps
        """
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


if __name__ == "__main__":
    ship = ShipPart1()
    ship.execute_all_instructions(INSTRUCTIONS)
    print(ship.get_manhattan_distance())
