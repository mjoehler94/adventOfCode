# day1 ----------------------------

def is_even(x):
    return x % 2 == 0


def file_to_list(file_path):
    output_list = []
    with open(file_path, 'r') as f:
        output_list = list(map(int, f.read().split()))

    return output_list


# needs to be increasing
# can't have two odds or two evens next to each other
def solve_puzzle1(inp):
    curr_streak = 1
    max_streak = 1
    for i in range(len(inp) - 1):
        # print(i, "|",inp[i], "|", curr_streak)
        if inp[i + 1] <= inp[i]:
            curr_streak = 1
            continue
        if (is_even(inp[i]) and is_even(inp[i+1])) or (not is_even(inp[i]) and not is_even(inp[i + 1])):
            curr_streak = 1
            continue
        curr_streak += 1
        max_streak = curr_streak if curr_streak > max_streak else max_streak
    return max_streak

def prep_list(inp_list):
    """
    returns the list that is optimized for the longest streak
    :param inp_list:
    :return:
    """
    # make a copy of the list to preserve the original
    inp_list = [x for x in inp_list]
    inp_list.sort()

    curr_ind = 0
    next_ind = 1
    while next_ind < len(inp_list):
        a = inp_list[curr_ind]
        b = inp_list[next_ind]
        if inp_list[curr_ind] == inp_list[next_ind] or is_even(inp_list[curr_ind]) == is_even(inp_list[next_ind]):
            inp_list.pop(next_ind)
            continue
        curr_ind += 1
        next_ind += 1
    print(len(inp_list))
    return inp_list


# MAIN ------------------------------------------
def main():

    test_list = [1, 2, 3, 4, 1, 2, 3]

    x = solve_puzzle1(test_list)
    print(x)

    input_list = file_to_list('data/raw1.txt')
    print('input list', len(input_list))
    y = solve_puzzle1(input_list)
    print(y)

    # test_list2 = [8, 8, 8, 5, 5, 3]
    # new_list = prep_list(test_list2)
    new_list = prep_list(input_list)
    print('new_list',len(new_list))
    print('new_list', new_list)
    print('old_list', input_list)
    z = solve_puzzle1(new_list)
    print(z)

    return


if __name__ == "__main__":
    main()
