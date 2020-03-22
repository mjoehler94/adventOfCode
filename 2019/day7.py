# day 7 ----------------------------------------
"""
     O-------O  O-------O  O-------O  O-------O  O-------O
0 -> | Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
    O-------O  O-------O  O-------O  O-------O  O-------O

    The program asks for phase code first, then input which comes from previous Amplifier (0 for first amplifier)
"""

from itertools import permutations
from IntCodeComputer import IntCodeComputer


def get_inputs(path):
    with open(path) as f:
        input_values_raw = f.read().strip('\n').split(',')
    input_values = [int(i) for i in input_values_raw]
    return input_values


def solve_puzzle1(inputs):
    # create permutations
    phase_codes = [0, 1, 2, 3, 4]
    sequences = permutations(phase_codes)
    seq_list = list(sequences)

    # loop through and return max output
    thruster_outputs = []
    for seq in seq_list:
        # print(seq)
        ampA = IntCodeComputer(inputs)
        ampA.input_values = [seq[0], 0]
        ampA.run_program()

        ampB = IntCodeComputer(inputs)
        ampB.input_values = [seq[1], ampA.output_values[0]]
        ampB.run_program()

        ampC = IntCodeComputer(inputs)
        ampC.input_values = [seq[2], ampB.output_values[0]]
        ampC.run_program()

        ampD = IntCodeComputer(inputs)
        ampD.input_values = [seq[3], ampC.output_values[0]]
        ampD.run_program()

        ampE = IntCodeComputer(inputs)
        ampE.input_values = [seq[4], ampD.output_values[0]]
        ampE.run_program()

        thruster_outputs.append(ampE.output_values[0])
    print(thruster_outputs, len(thruster_outputs))
    return max(thruster_outputs)


def solve_puzzle2(inputs):
    # create permutations
    phase_codes = [5, 6, 7, 8, 9]
    sequences = permutations(phase_codes)
    seq_list = list(sequences)

    # for each sequence
    # loop through and return max output
    thruster_outputs = []
    for seq in seq_list:
        # initialize amplifiers
        ampA = IntCodeComputer(inputs)
        ampB = IntCodeComputer(inputs)
        ampC = IntCodeComputer(inputs)
        ampD = IntCodeComputer(inputs)
        ampE = IntCodeComputer(inputs)

        # use while loop for feedback loop
        halted = 0
        first_iter = True
        while not halted:
            ampA.input_values = [seq[0], 0] if first_iter else [ampE.output_values]
            ampA.run_program()

            ampB.input_values = [seq[1], ampA.output_values[0]] if first_iter else ampA.output_values
            ampB.run_program()

            ampC.input_values = [seq[2], ampB.output_values[0]] if first_iter else ampB.output_values
            ampC.run_program()

            ampD.input_values = [seq[3], ampC.output_values[0]] if first_iter else ampC.output_values
            ampD.run_program()

            ampE.input_values = [seq[4], ampD.output_values[0]] if first_iter else ampD.output_values
            ampE.run_program()
            halted = ampA.is_halted + ampB.is_halted + ampC.is_halted + ampD.is_halted + ampE.is_halted
            first_iter = False

        thruster_outputs.append(ampE.output_values[0])
    # print(thruster_outputs, len(thruster_outputs))
    return max(thruster_outputs)


def main():
    file_location = 'data/input7.txt'
    input_values = get_inputs(file_location)
    # print(f"Input: {input_values}")

    # print(run_int_code(input_values, other_inputs=[1,2]))

    code = [0, 1, 2, 3, 4]
    sequences = permutations(code)
    seq_list = list(sequences)
    # print(sequences)
    # print(len(seq_list), seq_list[:5])

    # print("Puzzle1:", solve_puzzle1(input_values))  # 206580
    test_inputs = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
    print("Puzzle2:", solve_puzzle2(test_inputs))  # test_input answer should be 139629729

    return


if __name__ == "__main__":
    main()
