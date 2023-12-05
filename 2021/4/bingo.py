from sys import argv

import numpy as np


def task_1(data_in):
    data = data_in.split('\n')
    draws = data[0].split(',')

    boards = []

    for i in range(int(len(data[2:]) / 6)):
        offset = 2 + i * 6
        board = np.loadtxt(data[offset:offset+6])
        print(board)
        boards.append(board)

    bingo = None
    last_draw = None
    for draw in draws:
        number = int(draw)
        for board in boards:
            board[board == number] = 0
            if 0 in board.sum(axis=0) or 0 in board.sum(axis=1):
                bingo = board
                print(bingo)
                last_draw = number
                break
        if not bingo is None:
            break

    return last_draw, int(bingo.sum())

def task_2(data_in):
    data = data_in.split('\n')
    draws = data[0].split(',')

    boards = []

    for i in range(int(len(data[2:]) / 6)):
        offset = 2 + i * 6
        board = np.loadtxt(data[offset:offset + 6])
        print(board)
        boards.append(board)

    bingo = None
    last_draw = None
    next_boards = []
    for draw in draws:
        number = int(draw)
        for board in boards:
            board[board == number] = 0
            if 0 in board.sum(axis=0) or 0 in board.sum(axis=1):
                if len(boards) == 1:
                    bingo = board
                    print(bingo)
                    last_draw = number
                    break
            else:
                next_boards.append(board)
        if not bingo is None:
            break
        else:
            boards = next_boards
            next_boards = []

    return last_draw, int(bingo.sum())


if __name__ == "__main__":
    if len(argv) < 2:
        file = "input.txt"
    else:
        file = argv[1]

    data = open(file)
    last, bingo_sum = task_2(data.read())
    print("Last: " + str(last) + " | Bingo: " + str(bingo_sum))
    print("Result: " + str(last * bingo_sum))