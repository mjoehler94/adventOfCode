def main():
    with open("puzzle_inputs/day1.txt") as f:
        pi = f.read().split("\n")

    vals = []
    temp = []
    for calories in pi:
        if calories == "":
            vals.append(temp)
            temp = []
        else:
            temp.append(int(calories))
    else:
        if len(temp):
            vals.append(temp)

    print(max(vals, key=sum), sum(max(vals, key=sum)))

    print()
    cals = [sum(x) for x in vals]

    print(sum(sorted(cals)[-3:]))


if __name__ == "__main__":
    main()
