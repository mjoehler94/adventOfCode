# day 5 -----------------------------------


def get_inputs(path):
    with open(path) as f:
        input_values_raw = f.read().strip('\n').split(',')
    input_values = [int(i) for i in input_values_raw]
    return input_values


def run_int_code(inputs):
    # make a copy of the list so as to not modify the original
    inputs = [i for i in inputs]

    i = 0
    while True:
        # check code and handle accordingly
        raw_code = str(inputs[i]).zfill(5)
        code = int(raw_code[-2:])
        mode1 = int(raw_code[2])
        mode2 = int(raw_code[1])
        # mode3 = int(raw_code[0])

        if code == 99:
            print("End Code 99 Reached")
            break
        # otherwise perform operations
        if code in [1, 2]:
            param1 = inputs[i + 1]
            param2 = inputs[i + 2]
            param3 = inputs[i + 3]

        if code == 1:  # add
            val1 = inputs[param1] if mode1 == 0 else param1
            val2 = inputs[param2] if mode2 == 0 else param2
            inputs[param3] = val1 + val2
            i += 4
        elif code == 2:  # multiply
            val1 = inputs[param1] if mode1 == 0 else param1
            val2 = inputs[param2] if mode2 == 0 else param2
            inputs[param3] = val1 * val2
            i += 4
        elif code == 3:  # take user input
            param1 = inputs[i + 1]  # don't include mode because it's a write instruction
            input_num = input("Provide integer for input: ")
            inputs[param1] = int(input_num)
            i += 2
        elif code == 4:  # print parameter
            param1 = inputs[i + 1]
            val1 = inputs[param1] if mode1 == 0 else param1
            print(val1)
            i += 2

        elif code in [5, 6]:
            param1 = inputs[i + 1]
            param2 = inputs[i + 2]
            val1 = inputs[param1] if mode1 == 0 else param1
            val2 = inputs[param2] if mode2 == 0 else param2
            if code == 5:  # jump if true
                if val1 != 0:
                    inputs[i] = val2
                    i = val2
                    continue
            elif code == 6:  # jump if false
                if val1 == 0:
                    # inputs[i] = val2
                    i = val2
                    continue
            i += 3
        elif code in [7, 8]:
            param1 = inputs[i + 1]
            param2 = inputs[i + 2]
            param3 = inputs[i + 3]
            val1 = inputs[param1] if mode1 == 0 else param1
            val2 = inputs[param2] if mode2 == 0 else param2
            if code == 7:  # less than
                inputs[param3] = 1 if val1 < val2 else 0
            elif code == 8:  # less than
                inputs[param3] = 1 if val1 == val2 else 0
            i += 4
        else:
            # print(i, inputs[i])
            print("Error: Invalid IntCode")
            break
    return


def solve_puzzle1(input_list):
    return run_int_code(input_list)


def solve_puzzle2(input_list):
    return run_int_code(input_list)


def main():
    file_location = 'data/input5.txt'
    input_values = get_inputs(file_location)
    # print(f"Input: {input_values}")

    # test_inputs3 = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
    #                 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
    #                 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

    # solve_puzzle2(test_inputs3)

    # solve_puzzle1(input_values)  # 15426686
    solve_puzzle2(input_values)  # 11430197

    return


if __name__ == "__main__":
    main()
