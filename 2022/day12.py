def pathfinder(row, col, grid):
    n_rows = len(grid)
    n_cols = len(grid[row])
    global p1

    # base case
    if row < 0 or row > n_rows - 1 or col < 0 or col > n_cols - 1:
        # out of bounds
        return False
    elif grid[row][col] == "E":
        # is the end
        p1.append((row, col))
        return True

    # find a step from each neighbor
    else:
        pass


def main():
    # read in puzzle input
    day = 12
    with open(f"puzzle_inputs/day{day}.txt") as f:
        pi = [x.strip() for x in f.readlines()]

    samp = """Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi"""
    pi = [x.strip() for x in samp.split("\n")]
    print(len(pi))
    print(pi[:5])

    nrows = len(pi)
    ncols = len(pi[0])
    print(nrows, ncols)
    p1 = []

    start = -1
    end = -1
    for ri in range(len(pi)):
        for ci in range(len(pi[ri])):
            if pi[ri][ci] == "S":
                start = (ri, ci)
            if pi[ri][ci] == "E":
                end = (ri, ci)

    print(start, end)

    total = 0
    total2 = 0

    # solve 1
    for item in pi:
        pass

    # solve 2
    for item in pi:
        pass


if __name__ == "__main__":
    main()
