def main():
    # read in puzzle input
    day = 4
    with open(f"puzzle_inputs/day{day}.txt") as f:
        pi = [x.strip() for x in f.readlines()]

    print(len(pi))
    print(pi[:5])

    # solve 1
    total = 0
    total2 = 0
    for item in pi:
        a, b = item.split(",")
        a1, a2 = [int(num) for num in a.split("-")]
        b1, b2 = [int(num) for num in b.split("-")]

        # logic for part 1
        if a1 <= b1 and a2 >= b2:
            total += 1
        elif b1 <= a1 and b2 >= a2:
            total += 1

        # logic for part 2
        if a1 <= b1 and a2 >= b1:
            total2 += 1
        elif b1 <= a1 and b2 >= a1:
            total2 += 1
    print(total)
    print(total2)


if __name__ == "__main__":
    main()
