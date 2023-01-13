import random

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def make_move(board,player):
    available_moves = [(x,y) for x in range(3) for y in range(3) if board[x][y] == ' ']
    if not available_moves:
        return None
    move = random.choice(available_moves)
    x,y = move
    board[x][y] = player
    return move