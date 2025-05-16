import random
import sys
import argparse
#rules of game of life:
#1 if cell is alive, it stays alive if it has 2 or 3 live neighbors
#2 cells come to life only when surrounded by 3 live neighbors
def print_board(board):
    print("----------")
    for row in board:
        for col in row:
            print(col, end=" ")
        print("")
    print("----------")

def update_board(board, board2):
    for y in range(len(board)):
        for x in range(len(board[0])):
            board2[y][x] = next_state(x, y, board)


def next_state(x,y, board):
    life_juice = 0 

    for row in range(y-1, y+2):
        for col in range(x-1, x+2):
            life_juice += get_state(col, row, board)
    life_juice -= board[y][x]

    if board[y][x] == 0:
        if life_juice == 3:
            return 1
        return 0

    if life_juice == 2 or life_juice == 3:
        return 1
    return 0

def get_state(x, y, board):
    if x < 0 or y < 0 or x >= len(board[0]) or y >= len(board):
        return 0
    return board[y][x]

def main():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument(
        "--generations",
        type=int,
        default=5,
        help="Number of generations to simulate (default: 5)"
    )
    args = parser.parse_args()
    generations = args.generations

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    board2 = [[0] * 10 for _ in range(10)]

    print_board(board)
    for _ in range(generations):
        update_board(board, board2)
        print_board(board2)
        board, board2 = board2, board

main()
