def main():
    # read in puzzle input
    day = 6
    with open(f"puzzle_inputs/day{day}.txt") as f:
        pi = f.read()  # [x.strip() for x in f.readlines()]

    total = 0
    total2 = 0

    # pi = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

    # solve 1
    for i in range(len(pi)):
        # print(i)
        if i < 4:
            total += 1
        elif len(set(pi[i - 4 : i])) == 4:
            print(pi[i - 4 : i])
            break
        else:
            total += 1

    print("1:", total)

    # solve 2
    for i in range(len(pi)):
        # print(i)
        if i < 14:
            total2 += 1
        elif len(set(pi[i - 14 : i])) == 14:
            print(pi[i - 14 : i])
            break
        else:
            total2 += 1

    print("2:", total2)


if __name__ == "__main__":
    main()
