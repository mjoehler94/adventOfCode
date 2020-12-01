# IntCodeComputer --------------------------------------------------

"""
This class is designed based on various descriptions scattered across several of the intructions for
days 2, 5, 7, and probably more to come.
For days 2 and 5 I used an intcode computer function instead of a class. Day 7 is more complex, and after multiple
failed attempts, I decided to draft this class at the wise suggestion of my older brother who is a much better programmer
than myself.
"""


class IntCodeComputer(object):
    def __init__(self, program_code):
        self.program = program_code  # should be a list of integers
        self.current_memory = program_code.copy()
        self.instruction_pointer = 0  # start at beginning of list
        self.output_values = []  # a list to store the codes from output 4
        self.input_values = []  # a list to store input numbers
        self.is_halted = 0
        return

    # def reset(self):
    #     self.current_memory = self.program.copy()
    #     self.instruction_pointer = 0  # start at beginning of list
    #     return

    def run_program(self):
        inputs = self.current_memory

        # i = self.instruction_pointer
        while True:
            # check code and handle accordingly
            raw_code = str(inputs[i]).zfill(5)
            code = int(raw_code[-2:])
            mode1 = int(raw_code[2])
            mode2 = int(raw_code[1])
            # mode3 = int(raw_code[0])

            if code == 99:
                print("End Code 99 Reached")
                self.is_halted = 0
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
                # input_num = input("Provide integer for input: ")
                input_num = self.input_values.pop(0)

                inputs[param1] = int(input_num)
                i += 2
            elif code == 4:  # print parameter
                param1 = inputs[i + 1]
                val1 = inputs[param1] if mode1 == 0 else param1
                self.output_values.append(val1)
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
