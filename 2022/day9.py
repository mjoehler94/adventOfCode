class Grid:
    def __init__(self) -> None:
        self.head = {"x": 0, "y": 0}
        self.tail = {"x": 0, "y": 0}
        self.tail_path = [str(self.tail)]
        self.p1 = None

    def do_step(self, direction, dist):
        if direction == "R":
            for i in range(dist):
                self.head["x"] += 1
                self.update_tail()
        elif direction == "U":
            for i in range(dist):
                self.head["y"] += 1
                self.update_tail()

        elif direction == "L":
            for i in range(dist):
                self.head["x"] -= 1
                self.update_tail()
        elif direction == "D":
            for i in range(dist):
                self.head["y"] -= 1
                self.update_tail()

    def update_tail(self):
        x_diff = abs(self.head["x"] - self.tail["x"])
        y_diff = abs(self.head["y"] - self.tail["y"])
        if x_diff + y_diff > 2:
            # move diagonally
            self.tail["x"] += 1 if self.head["x"] > self.tail["x"] else -1
            self.tail["y"] += 1 if self.head["y"] > self.tail["y"] else -1
        elif x_diff > 1:
            # move horizontally
            self.tail["x"] += 1 if self.head["x"] > self.tail["x"] else -1
        elif y_diff > 1:
            # move vertically
            self.tail["y"] += 1 if self.head["y"] > self.tail["y"] else -1

        self.tail_path.append(str(self.tail))

    def part1(self, pi):
        for x in pi:
            direction = x[0]
            dist = int(x[1])
            self.do_step(direction, dist)

        self.p1 = len(set(self.tail_path))


class Knot:
    def __init__(self, tail=None) -> None:
        self.x = 0
        self.y = 0
        self.tail = tail
        self.path = []  # gets updated by its head, not by itself

    # only use this method if it's the main head
    def do_move(self, direction, dist):
        if direction == "R":
            for i in range(dist):
                self.x += 1
                self.update_tail()
        elif direction == "U":
            for i in range(dist):
                self.y += 1
                self.update_tail()
        elif direction == "L":
            for i in range(dist):
                self.x -= 1
                self.update_tail()
        elif direction == "D":
            for i in range(dist):
                self.y -= 1
                self.update_tail()

    # all tails will do this for their heads
    def update_tail(self):
        if self.tail is None:
            return
        x_diff = abs(self.x - self.tail.x)
        y_diff = abs(self.y - self.tail.y)
        if x_diff + y_diff > 2:
            # move diagonally
            self.tail.x += 1 if self.x > self.tail.x else -1
            self.tail.y += 1 if self.y > self.tail.y else -1
        elif x_diff > 1:
            # move horizontally
            self.tail.x += 1 if self.x > self.tail.x else -1
        elif y_diff > 1:
            # move vertically
            self.tail.y += 1 if self.y > self.tail.y else -1

        self.tail.path.append(str(self.tail))
        self.tail.update_tail()

    def __repr__(self):
        return f"(x:{self.x}, y:{self.y})"

    def run(self, pi):
        # this function exectur
        for x in pi:
            direction = x[0]
            dist = int(x[1])
            self.do_move(direction, dist)


def main():
    # read in puzzle input
    day = 9
    with open(f"puzzle_inputs/day{day}.txt") as f:
        pi = [x.strip().split() for x in f.readlines()]

    samp = """R 4
        U 4
        L 3
        D 1
        R 4
        D 1
        L 5
        R 2"""
    # pi = [x.strip().split() for x in samp.split("\n")]

    # print(len(pi))
    # print(pi[:10])

    total = 0
    total2 = 0

    # solve 1
    p1 = Grid()
    p1.part1(pi)
    # print(*p1.tail_path, sep="\n")
    print(p1.p1)

    print()
    # print(p1.tail_path)

    # solve 2
    samp2 = """R 5
        U 8
        L 8
        D 3
        R 17
        D 10
        L 25
        U 20"""

    # pi = [x.strip().split() for x in samp2.split("\n")]
    print(pi[:5])
    print()

    n_knots = 10
    knots = [Knot() for i in range(n_knots)]
    for i in range(n_knots - 1):
        knots[i].tail = knots[i + 1]

    head = knots[0]
    tail = knots[-1]
    head.run(pi)

    print(*knots)
    print([knot.tail for knot in knots])
    print()
    print(tail.path)

    print(len(set(tail.path)))

    #

    # now there are 10 total knots 1 head and 9 tails where each tail is the head for the tail after itself


if __name__ == "__main__":
    main()
