import os
import sys
from typing import List, Tuple

from conf import ROOT_DIR

sys.setrecursionlimit(1500)


BOOT_CODE_PATH = os.path.join(ROOT_DIR, "day_8/boot_code.txt")


def get_boot_code(filepath: str = BOOT_CODE_PATH) -> List[str]:
    """
    read the file containing the exercise challenge data and return an iterable of the contents
    :param filepath: path to file
    :return: generator expression yielding lines of boot code
    """
    with open(filepath) as file:
        return [line.strip() for line in file.readlines()]


def parse_line(line: str) -> Tuple[str, int]:
    """
    parse the operation and argument from a line of code
    :param line: line of code
    :return: operation and argument
    """
    operation, argument = line.split()
    return operation, int(argument)


def parse_code(code: List[str]) -> List[Tuple[str, int]]:
    """
    parse every line of code in a list
    :param code: list of code lines
    :return: list of operation:argument pairs
    """
    return [parse_line(line) for line in code]


class BootCode:
    def __init__(self, code: List[str]):
        """
        instances of BootCode keep track of the code's running state
        :param code: list of code lines
        """
        self.code = parse_code(code)
        self.accumulator = 0
        self.index = 0
        self.index_run_counts = [0 for _ in range(len(self.code))]
        self.terminated = False

    def nop(self, argument: int):
        """
        the nop operation ignores 'argument' and calls jmp(1), jumping to the next line
        """
        self.jmp(1)

    def jmp(self, argument: int):
        """
        the jmp operation increments the code line by the argument value and calls run so the code jumps to that line
        """
        self.index += argument
        self.run()

    def acc(self, argument: int):
        """
        the acc operation increments the accumulator by the argument value and calls jmp(1), jumping to the next line
        """
        self.accumulator += argument
        self.jmp(1)

    def run(self):
        """
        the run operation runs the operation at the current index, with the respective argument.
        each time a line of code is run the index_run_count is incremented.
        if index_run_count exceeds 1 the run halts, and self.terminated remains False.
        if run reaches an index which is out of bounds (i.e. the end of the program),
        then self.terminated is set to True.
        """
        try:
            operation, argument = self.code[self.index]
            self.index_run_counts[self.index] += 1
            if self.index_run_counts[self.index] > 1:
                pass
            else:
                eval(f"self.{operation}({argument})")
        except IndexError:
            self.terminated = True
