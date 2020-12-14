import os
from typing import List, Tuple, Union

from conf import ROOT_DIR

SCHEDULE_PATH = os.path.join(ROOT_DIR, "day_13/schedule.csv")


def get_schedule(filepath: str = SCHEDULE_PATH) -> Tuple[int, List[Union[int, str]]]:
    """
    read the file containing the exercise challenge data and return the departure time and the buses in service
    :param filepath: path to file
    :return: list of instructions as strings
    """
    with open(filepath) as file:
        departure_time, schedule = file.read().split()
        return int(departure_time), [
            int(bus) if bus != "x" else "x" for bus in schedule.split(",")
        ]
