from typing import List

from day_8.utils import BootCode, get_boot_code


def get_accumulator(code: List[str]):
    """
    get the accumulator value at the point at which the same line is about to be repeated
    :param code: ordered lines of code
    :return: accumulator value
    """
    boot_code = BootCode(code)
    boot_code.run()
    return boot_code.accumulator


if __name__ == "__main__":
    print(get_accumulator(get_boot_code()))
