# first day first puzzle -----------------

"""
Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:
For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement.

To find it, individually calculate the fuel needed for the mass
of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""

# libraries
# import pandas as pd


def calculate_fuel_needed(list_of_masses):
    """
    calculates the total fuel needed for all modules based on their mass values in the provided list
    :param list_of_masses: list of numbers representing the mass for each module
    :return: sum of fuel needed for all modules
    """
    fuel_values = []
    for m in list_of_masses:
        val = m // 3 - 2
        fuel_values.append(val)
    # print(fuel_values)

    return sum(fuel_values)


def calculate_needed_fuel_2(list_of_masses):
    fuel_values = []
    extra_fuel_values = []

    for m in list_of_masses:
        val = m // 3 - 2
        # fuel_values.append(val)
    # print(fuel_values)
        temp_extra_fuel = calculate_fuel_needed([val])
        total_extra_fuel = temp_extra_fuel
        while temp_extra_fuel > 0:
            temp_extra_fuel = calculate_fuel_needed([temp_extra_fuel])
            if temp_extra_fuel >= 0:
                total_extra_fuel += temp_extra_fuel  # if temp_extra_fuel >= 0 else 0
            # print(temp_extra_fuel)
        fuel_values.append(val + total_extra_fuel)

    return sum(fuel_values)


def get_inputs(path):
    """
    reads in data and stores it to a list which is then returned
    :param path: url or file path for module masses
    :return: python list of all the masses
    """
    input_values = []
    with open(path) as f:
        for line in f.readlines():
            input_values.append(int(line.rstrip('\n')))
    return input_values


def main():
    test_values = [12, 14, 1969, 100756]
    print(calculate_fuel_needed(test_values))

    real_values = get_inputs('data/input1.csv')
    # print(real_values[:5])
    print("Module Fuel:", calculate_fuel_needed(real_values))
    # print("Length:", len(real_values))

    # df = pd.read_csv('input.csv')
    # print(df.shape)
    # print(df.head(2))
    # module_fuel = calculate_fuel_needed(df.value)
    # print(module_fuel)
    # print(calculate_fuel_needed([module_fuel]))

    # part two calculate fuel needed for fuel
    # temp_extra_fuel = calculate_fuel_needed([module_fuel])
    # total_extra_fuel = 0
    # while temp_extra_fuel > 0:
    #     temp_extra_fuel = calculate_fuel_needed([temp_extra_fuel])
    #     if temp_extra_fuel >= 0:
    #         total_extra_fuel += temp_extra_fuel  # if temp_extra_fuel >= 0 else 0
    #     print(temp_extra_fuel)

    part2 = calculate_needed_fuel_2(real_values)

    # print("Total Module Fuel:", module_fuel)
    # print("Total Extra Fuel Needed:", total_extra_fuel)
    print("Grand Total:", part2)

    # 4894441 is too high

    return


if __name__ == "__main__":
    main()
