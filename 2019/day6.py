# day 6 --------------------------------------
# from collections import defaultdict


def get_input(path):
    input_list = []
    with open(path) as f:
        for line in f.readlines():
            input_list.append(line.strip('\n'))
    return input_list


def make_map(input_list):
    map_dict = dict()  # defaultdict(lambda: "")
    map_dict['COM'] = ""  # Center of Mass doesn't orbit anything
    for orbit in input_list:
        try:
            planet, moon = orbit.split(')')
            map_dict[moon] = planet
        except IOError as e:
            print(f"Invalid input: {orbit}")
            map_dict = None
    return map_dict


def count_orbits(map_dict):
    counter = 0
    for moon in map_dict.keys():
        planet = map_dict[moon]
        while planet != "":
            counter += 1
            planet = map_dict[planet]
    return counter


def get_orbit_path(orbit_map, start, end='COM'):
    # path list doesn't include starting point or ending point
    path_list = []
    planet = orbit_map[start]
    while planet != end:
        path_list.append(planet)
        planet = orbit_map[planet]
    return path_list


def solve_puzzle1(inputs):
    input_map = make_map(inputs)
    return count_orbits(input_map)


def solve_puzzle2(inputs):
    input_map = make_map(inputs)
    you_to_com = get_orbit_path(input_map, start='YOU', end='COM')
    san_to_com = get_orbit_path(input_map, start='SAN', end='COM')
    final_list = list(set(you_to_com).union(set(san_to_com)) - set(you_to_com).intersection(set(san_to_com)))
    # print(final_list)
    return len(final_list)


def main():
    # test cases ---------------------------------

    # puzzle 1
    # test_inputs1 = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
    # orbit_map = make_map(test_inputs1)
    # print(orbit_map)
    # print(count_orbits(orbit_map))
    
    # puzzle 2
    # test_inputs2 = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]
    # orbit_map2 = make_map(test_inputs2)
    # print(get_orbit_path(orbit_map2, start='YOU', end='COM'))
    # print(get_orbit_path(orbit_map2, start='SAN', end='COM'))
    # print(solve_puzzle2(test_inputs2))

    # puzzle input -------------------------------
    input_file = 'data/input6.txt'
    input_values = get_input(input_file)
    # print(len(input_values))
    print("Puzzle 1:", solve_puzzle1(input_values))
    print("Puzzle 2:", solve_puzzle2(input_values))

    return


if __name__ == '__main__':
    main()
