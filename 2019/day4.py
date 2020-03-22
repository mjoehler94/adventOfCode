# day 4 -----------------------------


def solve_puzzle1(input_values):
    solution_counter = 0
    for num in range(input_values[0], input_values[1]):
        # initialize conditions
        is_double = False
        is_non_decreasing = True
        # convert to string for checking
        num_as_string = str(num)
        for i in range(len(num_as_string) - 1):
            if num_as_string[i] == num_as_string[i + 1]:
                is_double = True
            if int(num_as_string[i]) > int(num_as_string[i + 1]):
                is_non_decreasing = False
        if is_double and is_non_decreasing:
            solution_counter += 1

    return solution_counter


def solve_puzzle2(input_values):
    solution_counter = 0
    for num in range(input_values[0], input_values[1]):
        # initialize conditions
        is_double = False
        is_non_decreasing = True
        # convert to string for checking
        num_as_string = str(num)
        for i in range(len(num_as_string) - 1):
            # this section is adjusted with the new info we have (only had to add one extra condition)
            # the added condition works because we know the digits are non-decreasing
            if num_as_string[i] == num_as_string[i + 1] and num_as_string.count(num_as_string[i]) == 2:
                is_double = True
            if int(num_as_string[i]) > int(num_as_string[i + 1]):
                is_non_decreasing = False
        if is_double and is_non_decreasing:
            solution_counter += 1

    return solution_counter


def main():
    input_values = [146810, 612564]
    print("Puzzle1:", solve_puzzle1(input_values))
    print("Puzzle2:", solve_puzzle2(input_values))


    return


if __name__ == "__main__":
    main()
