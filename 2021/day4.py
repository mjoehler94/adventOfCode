# get numbers first
with open("data/day4.txt") as f:
    numbers = f.readline()
    boards = f.read()

# numbers = [int(x) for x in numbers.split(',')]
print(numbers)
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

board_dict = make_boards(boards)
# print(board_dict)

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
            board_score = numbers[:-1] * sum([x for x in board if x not in numbers])
            break
        else:
            position += step
            


    # check cols
    position = 0
    while(not board_score and position < step):
        col = board[position::step]
        if all([num in numbers for num in col]):
            board_score = numbers[:-1] * sum([x for x in board if x not in numbers])
            break
        else:
            position += 1

    return board_score

# solve part 1

# for each number called check all boards for winners
for i in range(1,len(numbers)):
    for bnum, board in board_dict.items():
        score = score_board(numbers[:i],board)
        if score:
            print(score)
            break
print("Done")


