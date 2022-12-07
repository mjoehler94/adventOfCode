def fetch_from_dict(keys, my_dict):
    curr = my_dict
    val = curr
    for k in keys:
        val = curr[k]
        curr = val
    return val


def make_tree(out):
    master_tree = {}
    # parent_tree = master_tree
    parent_keys = []
    for o in out:
        tokens = o.split(" ")
        if tokens[0] == "$" and tokens[1] == "ls":
            # do nothing if ls command
            continue
        elif tokens[0] == "dir":
            continue
        elif tokens[0] == "$" and tokens[1] == "cd":
            # get folder name
            folder_name = tokens[2]

            if folder_name == "..":
                parent_keys.pop()
                continue

            # get place to put it and put it there
            dict_to_update = fetch_from_dict(parent_keys, master_tree)
            dict_to_update[folder_name] = {}

            # update parent keys
            parent_keys.append(folder_name)

        else:  # should only have files at this point
            try:
                folder_name = tokens[1]
                size = int(tokens[0])
                dict_to_update = fetch_from_dict(parent_keys, master_tree)
                dict_to_update[folder_name] = size
                # update_tree(tokens[1], size, parent_tree, master_tree)
            except:
                raise Exception(f"unconsidered outcome: {tokens}")

    return master_tree


def get_size_of_dict(item):
    size = 0
    for k, v in item.items():
        if isinstance(item[k], dict):
            size += get_size_of_dict(item[k])
        else:
            size += item[k]
    return size


def get_sizes(root_dict, sizes):
    # get size of root and add to list
    sizes.append(get_size_of_dict(root_dict))

    for k in root_dict.keys():
        if isinstance(root_dict[k], dict):
            get_sizes(root_dict[k], sizes)

    return sizes


def main():
    # read in puzzle input
    day = 7
    with open(f"puzzle_inputs/day{day}.txt") as f:
        pi = [x.strip() for x in f.readlines()]
    # print(len(pi))
    # print(pi[])

    # samp = """$ cd /
    #     $ ls
    #     dir a
    #     14848514 b.txt
    #     8504156 c.dat
    #     dir d
    #     $ cd a
    #     $ ls
    #     dir e
    #     29116 f
    #     2557 g
    #     62596 h.lst
    #     $ cd e
    #     $ ls
    #     584 i
    #     $ cd ..
    #     $ cd ..
    #     $ cd d
    #     $ ls
    #     4060174 j
    #     8033020 d.log
    #     5626152 d.ext
    #     7214296 k"""

    # samp = [x.strip() for x in samp.split("\n")]
    # pi = samp

    # print(len(pi))
    # print(pi)

    # solve 1
    tree = make_tree(pi)
    sizes = []
    get_sizes(tree, sizes)

    # print(sizes)
    max_size = 100_000
    print(sum([x for x in sizes if x < max_size]))

    # solve 2
    # print("\n\npart2 --------")
    total_space = 70_000_000
    target_unused_space = 30_000_000
    unused_space = total_space - get_size_of_dict(tree)

    best_option = None
    for s in sizes:
        if unused_space + s > target_unused_space:
            if best_option is None:
                best_option = s
            elif s < best_option:
                best_option = s
    print(best_option)
    # print(unused_space + best_option > target_unused_space)


if __name__ == "__main__":
    main()
