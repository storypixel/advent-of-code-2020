

import fileinput
from adventils import stacked2list


# de-nests things but stops at strings so we don't get ['t', 'h', 'i', 's']
def flatten(foo):
    for x in foo:
        if hasattr(x, '__iter__') and not isinstance(x, str):
            for y in flatten(x):
                yield y
        else:
            yield x


# Create a dictionary from the rules
def build_book(rules):
    book = dict()
    for ru in rules:
        container, contained = ru.split('contain')
        container = '_'.join(container.split()[:2])

        contained = contained.lstrip(' ').rstrip('.\n').split(',')

        items = []
        for item in contained:
            quant, *value = item.split()
            value = '_'.join(value[:2])

            num = False
            try:
                num = int(quant)
            except ValueError:
                num = False

            if num != False:
                obj = {'amt': int(quant), 'bag_name': value}
            else:
                obj = {'amt': 0, 'bag_name': None}

            items.append(obj)

        book[container] = items
    return book


def get_bags_for_rule(rule_book, rule):
    # print("testing bags for rule",  rule_book.get(rule))
    rule_bags = rule_book.get(rule)
    if rule_bags == None:
        return []
    return [bag.get('bag_name')
            for bag in rule_bags
            ]

# in part 1 i couldn't do a simple count so i stuffed the array and them just counted the items in the array as if i were putting bags in bags


def explode_bag(rule_book, mother, query, rule, bags_for_rule):
    # print(rule)
    if query in bags_for_rule:
        # print("matched with ", mother)
        return True
    new_bags_for_rule = []
    for i, bag in enumerate(bags_for_rule):
        new_bags = get_bags_for_rule(rule_book, bag)
        if new_bags and new_bags[0] != None:
            new_bags_for_rule.insert(i, new_bags)
    new_bags_for_rule = list(flatten(new_bags_for_rule))

    if query in new_bags_for_rule:
        # print("matched with ", mother)
        return True

    if new_bags_for_rule == []:
        return False

    return explode_bag(rule_book, mother, query, rule, new_bags_for_rule)


def solve(inp):
    rules = stacked2list(inp, str)
    rule_book = build_book(rules)
    # print("rule book", rule_book)
    query = 'shiny_gold'
    # queries_found = 0

    count = 0

    # part 1
    for rule in rule_book:
        bags_for_rule = get_bags_for_rule(rule_book, rule)
        res = explode_bag(rule_book, rule, query, rule, bags_for_rule)
        # print("matches were", res)
        if res:
            count = count + 1

    # part 2
    shiny_gold_contained_bags = rule_book.get('shiny_gold')
    total = tabulate_bags(rule_book, shiny_gold_contained_bags, 1)
    print("p2: bags inside", query, "were", total)

    return (count, total - 1)


# part 2 solver
def tabulate_bags(rule_book, bags, mult, total=0):
    for bag in bags:
        bag_name = bag.get("bag_name")
        bag_amt = bag.get("amt")
        if bag_name == None:
            continue
        bags_in_bag = rule_book.get(bag_name)
        # the "total +" keeps the total going between loop cycles
        total = total + tabulate_bags(rule_book, bags_in_bag, bag_amt) * mult

    return total + mult


if __name__ == '__main__':
    # part1
    print(solve(fileinput.input()))
