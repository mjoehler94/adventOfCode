def score_game(elf, me):
    # play game
    diff = elf - me
    if diff == 0:  # draw
        return me + 3
    elif diff in [-2, 1]:  # lose
        return me + 0
    elif diff in [-1, 2]:  # win
        return me + 6
    else:
        raise Exception("You done messed up")


def determine_my_shape(elf, outcome):
    if outcome == "draw":
        return elf
    elif outcome == "win":
        return elf + 1 if elf != 3 else 1
    elif outcome == "lose":
        return elf - 1 if elf != 1 else 3
    else:
        raise Exception("you done messed up again")


def main():

    key1 = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    key2 = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }
    key3 = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    # read input
    with open("puzzle_inputs/day2.txt") as f:
        pi = [x.split() for x in f.readlines()]

    print(len(pi))
    print(pi[:5])

    # solve 1
    scores = []
    for game in pi:
        elf = key2[key1[game[0]]]
        me = key2[key1[game[1]]]
        scores.append(score_game(elf, me))
    print(len(scores))
    print(sum(scores))

    # solve 2
    scores = []
    for game in pi:
        elf = key2[key1[game[0]]]
        outcome = key3[game[1]]
        me = determine_my_shape(elf, outcome)
        scores.append(score_game(elf, me))
    print(len(scores))
    print(sum(scores))


if __name__ == "__main__":
    main()
