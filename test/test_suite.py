from kata_3.tictactoe import create_board, random_move
import pytest


def test_create_board():
    board = create_board()
    assert len(board) == 3
    assert all (len(row) == 3 for row in board)
    assert all (all(cell == ' ' for cell in row) for row in board)

def test_random_move():
    board = [['X', 'O', ' '],
             [' ', 'X', 'O'],
             [' ', ' ', 'X']]
    assert random_move(board) in [(0,2), (1,0), (2,0), (2,1)]