def main():
    # read in puzzle input
    day = 10
    with open(f"puzzle_inputs/day{day}.txt") as f:
        pi = [x.strip() for x in f.readlines()]

    # solve 1
    X = 1
    cycle = 0
    results = [(0, 1)]  # intialize it with a single value to help with indexing later
    for item in pi:
        if item == "noop":
            cycle += 1
            results.append((cycle, X))
        else:
            for _ in range(2):
                cycle += 1
                results.append((cycle, X))
            X += int(item.split()[1])

    sig_strengths = [s[0] * s[1] for s in results[20::40]]
    # print(sig_strengths)
    print(sum(sig_strengths))

    # solve 2
    image = ""
    for c, X in results[1:]:
        crt_pos = (c - 1) % 40
        if crt_pos == 0:
            image += "\n"
        if abs(X - crt_pos) <= 1:
            image += "#"
        else:
            image += " "
    print(image)


if __name__ == "__main__":
    main()
