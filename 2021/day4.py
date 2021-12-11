# get numbers first
with open("data/day4.txt") as f:
    numbers = f.readline()
    boards = f.read()

numbers = [int(x) for x in numbers.split(',')]
print(numbers[:10])
# print(boards[:153])

# print(boards.split())

def make_boards(raw_boards):
    numbers = raw_boards.split()
    counter = 0
    board_num = 0
    board_dict = dict()
    step = 25

    while counter < len(numbers):
        board_dict[board_num] = [int(num) for num in numbers[counter:counter + step]]
        counter += step
        board_num += 1

    for board in board_dict.values():
        assert len(board) == 25
    
    return board_dict



# write function to check if solved
def score_board(numbers, board):
    # return false or score of board and final number
    board_score = 0
    # check rows
    step = 5
    position = 0
    while(position < len(board)):
        row = board[position:position + step]
        if all([num in numbers for num in row]):
            board_score = numbers[-1] * sum([x for x in board if x not in numbers])
            break
        else:
            position += step

    # check cols
    position = 0
    while(not board_score and position < step):
        col = board[position::step]
        if all([num in numbers for num in col]):
            board_score = numbers[-1] * sum([x for x in board if x not in numbers])
            break
        else:
            position += 1
    # print(type(numbers[-1]), numbers[-1])
    return board_score

# solve part 1
print("Part 1")
board_dict = make_boards(boards)
# print(board_dict)

def part1(numbers, board_dict):
    # for each number called check all boards for winners
    for i in range(1,len(numbers)):
        for bnum, board in board_dict.items():
            score = score_board(numbers[:i],board)
            if score:
                print(bnum, i)
                print(score)
                return
part1(numbers, board_dict)
print("Done\n")


# part 2
# which board will win last and what is it's score
def part2(numbers, boards):
    # for each board print winning position, and score
    boards = list(boards.values())
    score_of_last_board = 0
    max_turns_to_win = 0
    for i, b in enumerate(boards):
        for n in range(1,len(numbers)):
            score = 0
            score = score_board(numbers[:n], b)
            # print(f"board: {i}, number_position: {n}, score: {score}")
            if score:
                if n > max_turns_to_win:
                    # print(i, n)
                    max_turns_to_win = n
                    score_of_last_board = score
                break
    # print(b)
    # print(max_turns_to_win)
    # print(score_of_last_board)
    return score_of_last_board
                


print("Part 2")
# print(len(numbers))
# print(len(board_dict.values()))
p2 = part2(numbers, board_dict)

print(p2)
print('Done')

