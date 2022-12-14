import ast
from functools import cmp_to_key


def compare(left, right):
    # if both are ints
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    # both are lists
    elif isinstance(left, list) and isinstance(right, list):
        # get lengths
        llen = len(left)
        rlen = len(right)
        i = 0
        while i < llen and i < rlen:
            c = compare(left[i], right[i])
            if c == -1:
                return -1
            if c == 1:
                return 1
            i += 1
        if i == llen and i < rlen:
            return -1
        elif i == rlen and i < llen:
            return 1
        else:
            return 0
    # exactly one is an int
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])


def main():
    # read in puzzle input
    day = 13
    with open(f"puzzle_inputs/day{day}.txt") as f:
        # pi = [x.strip() for x in f.readlines()]
        pi = [x.split("\n") for x in f.read().split("\n\n")]

    samp = """[1,1,3,1,1]
        [1,1,5,1,1]

        [[1],[2,3,4]]
        [[1],4]

        [9]
        [[8,7,6]]

        [[4,4],4,4]
        [[4,4],4,4,4]

        [7,7,7,7]
        [7,7,7]

        []
        [3]

        [[[]]]
        [[]]

        [1,[2,[3,[4,[5,6,7]]]],8,9]
        [1,[2,[3,[4,[5,6,0]]]],8,9]"""

    # pi = [x.split("\n") for x in samp.split("\n\n")]

    # solve 1
    my_sum = 0

    for i, packet in enumerate(pi):
        left = eval(packet[0])
        right = eval(packet[1])
        if compare(left, right) == -1:
            my_sum += i + 1
    print(my_sum)

    # solve 2
    packets = [
        [[2]],
        [[6]],
    ]
    for item in pi:
        for packet in item:
            packets.append(eval(packet))
    packets = sorted(packets, key=cmp_to_key(lambda left, right: compare(left, right)))
    decoder1 = packets.index([[2]]) + 1
    decoder2 = packets.index([[6]]) + 1
    print(decoder1 * decoder2)


if __name__ == "__main__":
    main()
