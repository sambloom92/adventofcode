import os

from conf import ROOT_DIR
from day_12.utils import Ship, get_instructions

INSTRUCTIONS_PATH = os.path.join(ROOT_DIR, "day_12/instructions.csv")
INSTRUCTIONS = get_instructions(INSTRUCTIONS_PATH)


if __name__ == "__main__":
    ship = Ship()
    ship.execute_all_instructions(INSTRUCTIONS)
    print(ship.get_manhattan_distance())
