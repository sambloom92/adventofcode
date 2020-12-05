from day_3.utils import TobogganMapRow, get_map, multiply_trees_hit, step_through_map


def test_get_map():
    expected = [
        TobogganMapRow("..##..."),
        TobogganMapRow("#...#.."),
        TobogganMapRow(".#....#"),
        TobogganMapRow("..#.#.."),
    ]
    assert get_map("example_map_1.csv") == expected


def test_step_through_map():
    assert step_through_map(1, 1, get_map("example_map_2.csv")) == 2
    assert step_through_map(1, 3, get_map("example_map_2.csv")) == 7
    assert step_through_map(1, 5, get_map("example_map_2.csv")) == 3
    assert step_through_map(1, 7, get_map("example_map_2.csv")) == 4
    assert step_through_map(2, 1, get_map("example_map_2.csv")) == 2


def test_multiply_trees_hit():
    assert multiply_trees_hit(get_map("example_map_2.csv")) == 336
