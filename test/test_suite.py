from kata_3.tictactoe import create_board
import pytest


def test_create_board():
    board = create_board()
    assert len(board) == 3
    assert all (len(row) == 3 for row in board)
    assert all (all(cell == ' ' for cell in row) for row in board)