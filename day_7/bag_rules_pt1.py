from day_7.utils import Bag, get_bag_rules


def count_bags_that_can_contain_shiny_gold() -> int:
    """
    count how many distinct bag colours can ultimately contain at least shiny gold bag, excluding shiny gold itself
    :return: distinct count of bag colours
    """
    all_rules = get_bag_rules()
    return len(
        {
            colour
            for colour in all_rules.keys()
            if colour != "shiny gold"
            and Bag(colour, all_rules).can_contain_shiny_gold()
        }
    )


if __name__ == "__main__":
    print(count_bags_that_can_contain_shiny_gold())
