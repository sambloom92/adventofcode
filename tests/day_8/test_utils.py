import os
from unittest.mock import patch

import pytest

from conf import ROOT_DIR
from day_8.utils import BootCode, get_boot_code, parse_code, parse_line

EXAMPLE_BOOT_CODE_PATH = os.path.join(ROOT_DIR, "tests/day_8/example_boot_code.txt")


def test_get_boot_code():
    expected = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]
    actual = get_boot_code(EXAMPLE_BOOT_CODE_PATH)
    assert actual == expected


def test_parse_code():
    expected = [
        ("nop", 0),
        ("acc", 1),
        ("jmp", 4),
        ("acc", 3),
        ("jmp", -3),
        ("acc", -99),
        ("acc", 1),
        ("jmp", -4),
        ("acc", 6),
    ]
    actual = parse_code(get_boot_code(EXAMPLE_BOOT_CODE_PATH))
    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("parse_line('nop +0')", ("nop", 0)),
        ("parse_line('acc +1')", ("acc", 1)),
        ("parse_line('jmp +4')", ("jmp", 4)),
        ("parse_line('acc +3')", ("acc", 3)),
        ("parse_line('jmp -3')", ("jmp", -3)),
        ("parse_line('acc -99')", ("acc", -99)),
        ("parse_line('acc +1')", ("acc", 1)),
        ("parse_line('jmp -4')", ("jmp", -4)),
        ("parse_line('acc +6')", ("acc", 6)),
    ],
)
def test_parse_line(test_input, expected):
    assert eval(test_input) == expected


def test_bootcode_nop():
    instance = BootCode(get_boot_code(EXAMPLE_BOOT_CODE_PATH))
    with patch("day_8.utils.BootCode.run"):
        instance.nop(0)
    assert instance.accumulator == 0
    assert instance.index == 1


def test_bootcode_acc():
    instance = BootCode(get_boot_code(EXAMPLE_BOOT_CODE_PATH))
    with patch("day_8.utils.BootCode.run"):
        instance.acc(1)
    assert instance.accumulator == 1
    assert instance.index == 1


def test_bootcode_jmp():
    instance = BootCode(get_boot_code(EXAMPLE_BOOT_CODE_PATH))
    with patch("day_8.utils.BootCode.run") as mock_run:
        instance.jmp(1)
    assert instance.accumulator == 0
    assert instance.index == 1
    mock_run.assert_called()


def test_bootcode_run():
    instance = BootCode(get_boot_code(EXAMPLE_BOOT_CODE_PATH))
    instance.run()
    assert instance.accumulator == 5
    assert instance.index == 1
    assert instance.terminated is False


def test_bootcode_run_fixed():
    instance = BootCode(get_boot_code(EXAMPLE_BOOT_CODE_PATH))
    instance.code[-2] = "nop", -4
    instance.run()
    assert instance.accumulator == 8
    assert instance.index == 9
    assert instance.terminated is True
