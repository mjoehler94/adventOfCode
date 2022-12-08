def main():
    # read in puzzle input
    day = 8
    with open(f"puzzle_inputs/day{day}.txt") as f:
        pi = [x.strip() for x in f.readlines()]

    # samp = """30373
    # 25512
    # 65332
    # 33549
    # 35390"""
    # pi = [x.strip() for x in samp.split("\n")]

    # print(*pi[:5], sep="\n")
    # print()

    total = 0
    total2 = 0

    # solve 1
    n_rows = len(pi)
    for ri, row in enumerate(pi):
        for ci, tree in enumerate(row):
            if ri == 0 or ci == 0 or ri == n_rows - 1 or ci == len(row) - 1:
                # print(ri, ci, row[ci])
                total += 1
            else:
                tree = int(tree)
                left = [t for t in row[0:ci] if int(t) >= tree]
                right = [t for t in row[ci + 1 :] if int(t) >= tree]
                top = [t[ci] for t in pi[:ri] if int(t[ci]) >= tree]
                bottom = [t[ci] for t in pi[ri + 1 :] if int(t[ci]) >= tree]

                if (
                    len(left) == 0
                    or len(right) == 0
                    or len(top) == 0
                    or len(bottom) == 0
                ):
                    total += 1
            # print()

    print(total)

    # solve 2
    n_rows = len(pi)
    high = 0
    for ri, row in enumerate(pi):
        for ci, tree in enumerate(row):
            score = 0
            if ri == 0 or ci == 0 or ri == n_rows - 1 or ci == len(row) - 1:
                # all edges have view score of 0
                continue
            else:
                tree = int(tree)
                left = 0
                for ti in range(ci - 1, -1, -1):
                    left += 1
                    if int(row[ti]) >= tree:
                        break
                right = 0
                for ti in range(ci + 1, len(row)):
                    right += 1
                    if int(row[ti]) >= tree:
                        break
                top = 0
                for ti in range(ri - 1, -1, -1):
                    top += 1
                    if int(pi[ti][ci]) >= tree:
                        break
                bottom = 0
                for ti in range(ri + 1, len(pi)):
                    bottom += 1
                    if int(pi[ti][ci]) >= tree:
                        break

                score = left * right * top * bottom
                # print(ri, ci, row[ci], left, right, top, bottom, score)
                high = max(high, score)

    print(high)


if __name__ == "__main__":
    main()
