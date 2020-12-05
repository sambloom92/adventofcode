import os
from typing import Iterable, Tuple

from conf import ROOT_DIR

BOARDING_PASSES_PATH = os.path.join(ROOT_DIR, "day_5/boarding_passes.csv")


def get_boarding_passes(filepath: str = BOARDING_PASSES_PATH) -> Iterable[str]:
    """
    get all the boarding passes from the specified file, and return a generator expression
    :param filepath:
    :return:
    """
    with open(filepath) as file:
        return (boarding_pass.strip() for boarding_pass in file.readlines())


def parse_to_decimal(input_value: str) -> int:
    """
    convert a boarding pass row or column into a decimal number
    :param input_value: string containing either 'F' anf 'B' or 'L' and 'R'
    :return: the decimal number corresponding to the input value
    """
    in_table = "FBLR"
    out_table = "0101"
    translation_table = str.maketrans(in_table, out_table)
    return int(input_value.translate(translation_table), 2)


def get_row_id(row: int, col: int) -> int:
    """
    convert a row and column number into a row id
    :param row: row as a decimal number
    :param col: column as a decimal number
    :return: row_id
    """
    return row * 8 + col


def parse_boarding_pass(boarding_pass: str) -> int:
    """
    parse a boarding_pass string into decimal row_id
    :param boarding_pass: a boarding pass as a 10 character string
    :return: the corresponding row_id
    """
    row, col = boarding_pass[:7], boarding_pass[7:]
    row_num = parse_to_decimal(row)
    col_num = parse_to_decimal(col)
    row_id = get_row_id(row_num, col_num)
    return row_id
