import math


class Monkey:
    def __init__(self, notes) -> None:
        self.items = [int(x.replace(",", "")) for x in notes[1].split(" ")[4:]]
        self.operator = notes[2].split(" ")[-2]
        self.operator_amount = notes[2].split(" ")[-1]
        self.test_mod = int(notes[3].split(" ")[-1])
        self.target_t = int(notes[4].split(" ")[-1])
        self.target_f = int(notes[5].split(" ")[-1])
        self.group = None
        self.items_counter = 0

    def inspect(self, item, part=1):
        if self.operator_amount == "old":
            oa = item
        else:
            oa = int(self.operator_amount)

        if self.operator == "*":
            item *= oa
        elif self.operator == "+":
            item += oa

        # relief
        if part == 1:
            item //= 3
        elif part == 2:
            item %= self.super_mod

        # update inspection counter
        self.items_counter += 1

        return item

    def throw(self, item):
        if item % self.test_mod == 0:
            self.group[self.target_t].items.append(item)
        else:
            self.group[self.target_f].items.append(item)

    def take_turn(self, part=1):
        for item in self.items:
            item = self.inspect(item, part=part)
            self.throw(item)
        self.items = []

    def __repr__(self):
        return f"""
    Starting items: {self.items}
    Operation: new = old {self.operator} {self.operator_amount}
    Test: divisible by {self.test_mod}
      If true: throw to monkey {self.target_t}
      If false: throw to monkey {self.target_f}
    group: {len(self.group)}
    items inspected: {self.items_counter}"""


def main():
    # read in puzzle input
    day = 11
    with open(f"puzzle_inputs/day{day}.txt") as f:
        # pi = [x.strip() for x in f.readlines()]
        pi = f.read().split("\n\n")
    pi = [x.split("\n") for x in pi]

    samp = """"""
    # print(len(pi))
    # print(pi[:8])

    monkeys = [Monkey(notes) for notes in pi]
    for m in monkeys:
        m.group = monkeys
        # print(m)

    # solve 1
    rounds = 20
    for r in range(rounds):
        for i, m in enumerate(monkeys):
            m.take_turn(part=1)

    counts = sorted([m.items_counter for m in monkeys], reverse=True)
    print(counts)
    print(counts[0] * counts[1])

    # solve 2
    monkeys = [Monkey(notes) for notes in pi]
    super_mod = 1
    for m in monkeys:
        m.group = monkeys
        super_mod *= m.test_mod

    for m in monkeys:
        m.super_mod = super_mod

    rounds = 10_000
    for r in range(rounds):
        # print(r)
        for m in monkeys:
            m.take_turn(part=2)

    counts = sorted([m.items_counter for m in monkeys], reverse=True)
    print(counts)
    print(counts[0] * counts[1])

    # for m in monkeys:
    #     print(m)


if __name__ == "__main__":
    main()
