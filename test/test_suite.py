from kata_3.tictactoe import make_move, win_or_draw, play_game, main, print_board
import io 
from contextlib import redirect_stdout 

def test_make_move():
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    move = make_move(board, 'X')
    assert move in [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)] or move == None
    if move is not None:
        assert board[move[0]][move[1]]== 'X'

def test_win_or_draw():
    board = [['X', 'X', 'X'],
             [None, None, None],
             [None, None, None]]
    winner = win_or_draw(board)
    assert winner == 'X'

    board = [['O', 'X', 'X'],
             ['X', 'O', 'X'],
             ['O', 'X', 'O']]
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
    winner = play_game(board)
    expected_output = f"The winner is: {winner}\n" if winner else "It's draw\n"
    assert captured.strip() == expected_output.strip()


def test_print_board():
    board = [['X', 'O', 'X'],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    f = io.StringIO()
    with redirect_stdout(f):
        print_board(board)
    captured = f.getvalue()
    expected_output = '\n'.join([' '.join([str(cell) if cell is not None else ' ' for cell in row]) for row in board]) + '\n'
    assert captured == expected_output

