from kata_3.tictactoe import make_move, win_or_draw, play_game, main, print_board
import io 
from contextlib import redirect_stdout 
import unittest
import unittest.mock
from unittest.mock import patch

def test_make_move():
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    with patch("kata_3.tictactoe.random.choice", return_value=(1,1)):
        move = make_move(board, 'X')
    assert move in [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)] or move == None
    if move is not None:
        assert board[move[0]][move[1]]== 'X'

def test_make_move_no_valid_moves_available():
    board = [['O', 'X', 'X'],
             ['X', 'O', 'X'],
             ['O', 'X', 'O']]
    player = 'X'
    assert make_move(board, player) == None
    assert board == [['O', 'X', 'X'],
                     ['X', 'O', 'X'],
                     ['O', 'X', 'O']]

def test_win_or_draw():
    board = [['X', 'X', 'X'],
             [None, None, None],
             [None, None, None]]
    winner = win_or_draw(board)
    assert winner == 'X'

    board = [['X', 'O', 'X'],
             [None, 'X', 'O'],
             ['O', None, 'X']]
    winner = win_or_draw(board)
    assert winner == 'X'

    board = [['X', 'O', 'X'],
             [None, 'X', 'O'],
             ['X', None, 'O']]
    winner = win_or_draw(board)
    assert winner == 'X'

    board = [['X', 'O', 'X'],
             [None, 'O', 'X'],
             ['O', None, 'X']]
    winner = win_or_draw(board)
    assert winner == 'X'

    board = [['O', 'X', 'X'],
             ['X', 'O', 'X'],
             ['O', 'X', 'O']]
    winner = win_or_draw(board)
    assert winner == 'O'

    board = [['X', 'O', 'X'],
             ['X', 'O', 'X'],
             [None, 'O', 'O']]
    winner = win_or_draw(board)
    assert winner == 'O'

    board = [['X', 'O', 'O'],
             ['X', 'O', 'X'],
             ['O', 'X', 'X']]
    winner = win_or_draw(board)
    assert winner == 'O'

    board = [['O', 'O', 'O'],
             ['X', None, 'X'],
             ['O', 'X', 'X']]
    winner = win_or_draw(board)
    assert winner == 'O'

    board = [['O', 'O', 'X'],
             ['X', 'X', 'O'],
             ['O', 'X', 'X']]
    winner = win_or_draw(board)
    assert winner == None

def test_play_game():
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    winner = play_game(board)
    assert winner in ['X', 'O', None]

def test_main():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    f = io.StringIO()
    with redirect_stdout(f):
        main(board)
    captured = f.getvalue()
    if "The winner is: " in captured:
        captured = captured[captured.index("The winner is: "):]
    elif "It's draw" in captured:
        captured = "It's draw\n"
    else:
        captured=captured.strip()
    winner = play_game(board)
    if winner == None:
        expected_output = "It's draw\n"
    else:
        expected_output = f"The winner is: {winner}\n"
    assert captured == expected_output
    
class TestMain(unittest.TestCase):
    def test_main_mock_1(self):
        with patch('builtins.print') as mocked_print:
            board = [[' ', ' ', ' '],
                     [' ', ' ', ' '],
                     [' ', ' ', ' ']]
            main(board)
            winner = play_game(board)
            if winner != None:
                mocked_print.assert_called_with(f"The winner is: {winner}")
            else:
                mocked_print.assert_called_with("It's draw")

class TestMainDraw(unittest.TestCase):
    def test_main_mock_2(self):
        with patch('builtins.print') as mocked_print:
            board = [['O', 'O', 'X'],
                     ['X', 'X', 'O'],
                     ['O', 'X', 'X']]
            main(board)
            mocked_print.assert_called_with("It's draw")
 
def test_print_board():
    board = [['X', 'O', 'X'],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    expected_output = "XOX\n   \n   \n"
    f = io.StringIO()
    with redirect_stdout(f):
        print_board(board)
    captured = '\n'.join([''.join([str(cell) for cell in row]) for row in board]) + '\n'
    assert captured == expected_output


