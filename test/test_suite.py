from kata_3.tictactoe import create_board, make_move
import pytest


def test_create_board():
    board = create_board()
    assert len(board) == 3
    assert all (len(row) == 3 for row in board)
    assert all (all(cell == ' ' for cell in row) for row in board)

def test_make_move():
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    move = make_move(board, 'X')
    assert move in [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)] or move == None
    if move is not None:
        assert board[move[0]][move[1]]== 'X'