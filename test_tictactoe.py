import pytest
from tictactoe import TicTacToe

@pytest.fixture
def game():
    return TicTacToe()

def test_generate_board(game):
    board = game.generate_board()
    assert len(board) == 4
    assert len(board[0]) == 4
    assert all(all(cell == ' ' for cell in row) for row in board)

def test_horizontal_win(game):
    board = [
        ['X', 'X', 'X', 'X'],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ']
    ]
    assert game.check_winner(board) == 'X'

def test_vertical_win(game):
    board = [
        ['O', ' ', 'X', ' '],
        ['O', ' ', ' ', ' '],
        ['O', ' ', ' ', ' '],
        ['O', ' ', ' ', ' ']
    ]
    assert game.check_winner(board) == 'O'

def test_diagonal_right_win(game):
    board = [
        ['X', ' ', ' ', ' '],
        [' ', 'X', 'O', ' '],
        [' ', 'O', 'X', ' '],
        [' ', ' ', ' ', 'X']
    ]
    assert game.check_winner(board) == 'X'

def test_diagonal_left_win(game):
    board = [
        [' ', ' ', ' ', 'O'],
        [' ', ' ', 'O', ' '],
        [' ', 'O', ' ', ' '],
        ['O', ' ', ' ', ' ']
    ]
    assert game.check_winner(board) == 'O'

def test_box_win(game):
    board = [
        ['X', 'X', ' ', ' '],
        ['X', 'X', 'O', ' '],
        [' ', 'O', ' ', ' '],
        [' ', ' ', ' ', ' ']
    ]
    board_two = [
        ['X', 'X', ' ', ' '],
        ['X', 'O', 'O', ' '],
        [' ', 'X', 'O', 'O'],
        [' ', ' ', 'O', 'O']
    ]
    assert game.check_winner(board) == 'X'
    assert game.check_winner(board_two) == 'O'


def test_corners_win(game):
    board = [
        ['O', ' ', ' ', 'O'],
        [' ', 'X', 'X', ' '],
        [' ', 'X', ' ', ' '],
        ['O', ' ', ' ', 'O']
    ]
    assert game.check_winner(board) == 'O'

def test_full_board_no_winner(game):
    board = [
        ['X', 'O', 'X', 'X'],
        ['O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'X', 'O', 'O']
    ]
    assert game.check_winner(board) == None

def test_any_moves_left(game):
    board_yes = [
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X'],
        ['X', 'O', ' ', 'O'],
        ['X', 'X', 'O', 'O']
    ]
    board_no = [
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'X', 'O', 'O']
    ]
    # winner, so it should still be false
    board_no_two = [
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'X', 'O', 'X']
    ]

    assert game.any_moves_left(board_yes) == True
    assert game.any_moves_left(board_no) == False
    assert game.any_moves_left(board_no_two) == False

def test_is_game_over(game):
    board_yes = [
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X'],
        ['X', 'O', ' ', 'O'],
        ['X', 'X', 'O', 'O']
    ]
    board_no = [
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'X', 'O', 'O']
    ]
    # winner, so it should be true
    board_no_two = [
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'X', 'O', 'X']
    ]

    assert game.is_game_over(board_yes) == False
    assert game.is_game_over(board_no) == True
    assert game.is_game_over(board_no_two) == True