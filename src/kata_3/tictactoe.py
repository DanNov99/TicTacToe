import random

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def random_move(board):
    available_moves = [(x, y) for x in range(3) for y in range (3) if board[x][y] == ' ']
    return random.choice(available_moves)
