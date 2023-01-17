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

def win_or_draw(board):
    for i in range(3):
        if board[i] == ['X','X','X']:
            return 'X'
        if board[i] == ['O','O','O']:
            return 'O'
        if (board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X'):
            return 'X'
        if (board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O'):
            return 'O'
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        return 'X'
    if (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        return 'O'
    return None

def play_game(board):
    return 'X'