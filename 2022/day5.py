class Stack:
    def __init__(self, stack_lol) -> None:
        self.stacks = {}
        for stack_l in stack_lol:
            for i in range(len(stack_l)):
                box = stack_l[i]
                if stack_l[i] == "":
                    continue
                if not self.stacks.get(i + 1, False):
                    self.stacks[i + 1] = [box]
                else:
                    self.stacks[i + 1].append(box)

    def do_move(self, count, from_ind, to_ind):
        for i in range(count):
            temp = self.stacks[from_ind].pop()
            self.stacks[to_ind].append(temp)

    def do_move2(self, count, from_ind, to_ind):

        temp = self.stacks[from_ind][-count:]
        self.stacks[from_ind] = self.stacks[from_ind][:-count]
        for item in temp:
            self.stacks[to_ind].append(item)

    def __repr__(self):
        return str(self.stacks)

    def show(self):
        print()
        print(*self.stacks.values(), sep="\n")

        ans = ""
        for k, v in self.stacks.items():
            # print("v", v[-1])
            ans += v[-1]

        print(ans)
        print()


def main():
    # read in puzzle input
    day = 5
    with open(f"puzzle_inputs/day{day}.txt") as f:
        # pi = [x.strip() for x in f.readlines()]
        crates, pi = f.read().split("\n\n")

    print(crates)
    print()

    crates = crates.replace(" ", ".").split("\n")
    # print(crates)

    rev_crates = crates[:-1][::-1]
    print()
    # print(*rev_crates, sep="\n")
    new = []
    for row in rev_crates:
        test = [row[i : i + 4] for i in range(0, len(row), 4)]
        test = [t.replace(".", "") for t in test]
        test = [t.replace("[", "") for t in test]
        test = [t.replace("]", "") for t in test]
        # print(len(test))
        new.append(test)

    print()
    # print(new)

    stacks = Stack(new)
    stacks.show()

    # clean up procedure (count, from , to)
    pi_split = pi.split("\n")
    proc = [x.split(" ")[1::2] for x in pi_split]
    proc = [[int(y) for y in x] for x in proc]
    print(proc[:9])

    print()

    total = 0
    total2 = 0
    for item in proc:
        # solve 1
        stacks.do_move(*item)

    stacks.show()

    stacks = Stack(new)
    for item in proc:
        stacks.do_move2(*item)
    stacks.show()


if __name__ == "__main__":
    main()
