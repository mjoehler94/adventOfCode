def main():

    # read input
    with open("puzzle_inputs/day3.txt") as f:
        pi = [x.strip() for x in f.readlines()]
    print(len(pi))
    # print(pi[:5])
    # print([len(a) for a in pi[:10]])

    priorities = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # solve 1
    total = 0
    for sack in pi:
        mid = len(sack) // 2  # all inputs are of even length
        print(len(sack), mid, sack)
        common = list(set(sack[:mid]).intersection(set(sack[mid:])))[0]

        p = priorities.find(str(common))
        # print(p, common, str(common))
        total += p
    print()
    print(total)

    # solve 2
    total = 0
    for i in range(0, len(pi), 3):
        one = set(pi[i])
        two = set(pi[i + 1])
        three = set(pi[i + 2])
        common = list(one.intersection(two).intersection(three))[0]
        p = priorities.find(common)
        total += p
    print(total)


if __name__ == "__main__":
    main()
