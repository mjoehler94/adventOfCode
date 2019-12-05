# day 2 ---------------------------------------

def get_inputs(path):
    """
    reads in data and stores it to a list which is then returned
    :param path: url or file path for module masses
    :return: python list of all the masses
    """
    with open(path) as f:
        input_values_raw = f.read().strip('\n').split(',')
    input_values = [int(i) for i in input_values_raw]
    return input_values


def solve_puzzle1(inputs):
    inputs = [i for i in inputs]
    for i in range(0, len(inputs), 4):
        # print("i:", i)
        code = inputs[i]
        # check code and get positions
        if code != 99:
            pos1 = inputs[i + 1]
            pos2 = inputs[i + 2]
            pos3 = inputs[i + 3]
        elif code == 99:
            return inputs
        # perform operations
        # TODO: is there an edge case for overlapping positions
        if code == 1:  # add
            inputs[pos3] = inputs[pos1] + inputs[pos2]
        elif code == 2:  # multiply
            inputs[pos3] = inputs[pos1] * inputs[pos2]
        else:
            print(i, inputs[i])
            return "Error: Invalid IntCode"
        i += 4

    return inputs


def solve_puzzle2(inputs, expected_result=19690720):
    inputs = [i for i in inputs]
    inputs_reset = [i for i in inputs]
    for noun in range(100):
        for verb in range(100):
            inputs = inputs_reset
            inputs[1] = noun
            inputs[2] = verb
            results = solve_puzzle1(inputs)
            if results[0] == 19690720:
                print(f"Noun: {noun}, Verb: {verb}")
                return 100 * noun + verb

    return "Didn't find solution"


def main():
    test_values = [1, 0, 0, 0, 99]
    test_answer = solve_puzzle1(test_values)
    print(test_answer)

    # read input file and save to list
    real_values = get_inputs("data/input2.txt")
    real_values[1] = 12
    real_values[2] = 2
    real_answer1 = solve_puzzle1(real_values)
    print("Inputs:", real_values)
    print("Puzzle 1:", real_answer1)

    real_answer2 = solve_puzzle2(real_values)
    print("Puzzle 2:", real_answer2)

    return


if __name__ == "__main__":
    main()
