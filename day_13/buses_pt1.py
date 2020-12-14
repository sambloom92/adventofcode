import os
from typing import Dict, List, Tuple, Union

from conf import ROOT_DIR
from day_13.utils import get_schedule

SCHEDULE_PATH = os.path.join(ROOT_DIR, "day_13/schedule.csv")


def get_earliest_bus(departure_time: int, buses: List[int]) -> Tuple[int, int]:
    bus_departures = {bus: 0 for bus in buses}
    round_trips = 1
    available_buses: Dict[int, int] = {}
    while len(available_buses) != len(buses):
        bus_departures = {
            bus: bus * round_trips if time < departure_time else time
            for bus, time in bus_departures.items()
        }
        available_buses = {
            bus: time for bus, time in bus_departures.items() if time > departure_time
        }
        round_trips += 1
    first_bus = min(available_buses, key=available_buses.get)  # type: ignore[type-var]  # noqa: F821
    bus_time = available_buses[first_bus]
    return first_bus, bus_time


if __name__ == "__main__":
    departure_time, buses = get_schedule()
    in_service_buses: List[int] = [int(bus) for bus in buses if bus != "x"]
    bus_number, bus_time = get_earliest_bus(departure_time, in_service_buses)
    print((bus_time - departure_time) * bus_number)
