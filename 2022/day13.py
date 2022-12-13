import ast


def compare(left, right):
    # if both are ints
    if isinstance(left, int) and isinstance(right, int):
        print("ints", left, right)
        if right > left:
            return False
        elif left < right:
            return True

        # if equal continue comparing other elements
        else:
            print("equal int")
            # return True
    # both are lists
    elif isinstance(left, list) and isinstance(right, list):
        print("lists", left, right)
        # get lengths
        llen = len(left)
        rlen = len(right)
        is_left_shorter = llen < rlen
        is_right_shorter = llen > rlen

        for i in range(min(llen, rlen)):
            return compare(left[i], right[i])

        # if left is shorter then return true else return false
        if is_left_shorter:
            return True
        elif is_right_shorter:
            return False
        else:
            print("same")
            return True

    # exactly one is an int
    else:
        print("one", left, right, type(left), type(right))
        if isinstance(left, int) and isinstance(right, list):
            left = list(left)
            return compare(left, right)
        elif isinstance(left, list) and isinstance(right, int):
            right = list(right)
            return compare(left, right)
    # return True


def main():
    # read in puzzle input
    day = 13
    with open(f"puzzle_inputs/day{day}.txt") as f:
        # pi = [x.strip() for x in f.readlines()]
        pi = [x.split("\n") for x in f.read().split("\n\n")]

    samp = [
        [1, 1, 3, 1, 1],
        [1, 1, 5, 1, 1],
        [[1], [2, 3, 4]],
        [[1], 4],
        [9],
        [[8, 7, 6]],
        [[4, 4], 4, 4],
        [[4, 4], 4, 4, 4],
        [7, 7, 7, 7],
        [7, 7, 7],
        [],
        [3],
        [[[]]],
        [[]],
        [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
        [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
    ]
    print(len(pi))
    # print(pi[:5])

    # solve 1
    correct_inds = []
    l = samp[0]
    r = samp[1]
    print(l, r)
    print(compare(samp[0], samp[1]))

    # for item in pi:
    #     # print(item[0])
    #     left = ast.literal_eval(item[0])
    #     right = ast.literal_eval(item[0])
    #     print(left)
    #     pass

    # solve 2
    for item in pi:
        pass


if __name__ == "__main__":
    main()
