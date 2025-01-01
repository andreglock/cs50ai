"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    moves = moves_made(board)
    if moves % 2 == 0:
        return 'X'
    return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                actions.add((row, column))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    column = action[1]

    newBoard = deepcopy(board)

    if board[row][column] == EMPTY:
        newBoard[row][column] = player(board)
        return newBoard
    raise 'Invalid Move'


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Winner not possible before 5 moves:
    if moves_made(board) < 5:
        return None
    # Test if winning combination includes board[0][0]:
    if (board[0][0] != EMPTY):
        if (
            (board[0][0] == board[0][1] and board[0][0] == board[0][2]) or 
            (board[0][0] == board[1][0] and board[0][0] == board[2][0]) or
            (board[0][0] == board[1][1] and board[0][0] == board[2][2])
        ): 
            return board[0][0]
    # Test if winning combination includes board[0][1]:
    if (board[0][1] != EMPTY):
        if (
            board[0][1] == board[1][1] and board[0][1] == board[2][1]
        ): 
            return board[0][1]
    # Test if winning combination includes board[0][2]:
    if (board[0][2] != EMPTY):
        if (
            (board[0][2] == board[1][2] and board[0][2] == board[2][2]) or 
            (board[0][2] == board[1][1] and board[0][2] == board[2][0])
        ): 
            return board[0][2]
    # Test if winning combination includes board[1][0]:
    if (board[1][0] != EMPTY):
        if (
            board[1][0] == board[1][1] and board[1][0] == board[1][2]
        ): 
            return board[1][0]
    # Test if winning combination includes board[2][0]:
    if (board[2][0] != EMPTY):
        if (
            board[2][0] == board[2][1] and board[2][0] == board[2][2]
        ): 
            return board[2][0]
    # All possible winning scenarios are tested, return null:
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board): 
        return True
    isTerminal = moves_made(board) == 9
    return isTerminal


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    if winner(board) == 'O':
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if moves_made(board) == 0:
        return (1, 1)
    if moves_made(board) == 9:
        return None
    else:
        return find_best(board)


def moves_made(board):
    moves = 0
    for row in board:
        for square in row:
            if square != EMPTY:
                moves += 1
    return moves


def find_value(board):
    winner = utility(board)
    if winner != 0:
        return winner
    possible_actions = actions(board)
    if len(possible_actions) == 1:
        return utility(result(board, possible_actions.pop()))
    if player(board) == 'X':
        best = -2
        for action in possible_actions:
            best = max(best, find_value(result(board, action)))
    else:
        best = 2
        for action in possible_actions:
            best = min(best, find_value(result(board, action)))
    return best


def find_best(board):
    to_play = player(board)
    if to_play == 'X':
        best = -2
    else:
        best = 2
    best_action = (-1, -1)
    possible_actions = actions(board)
    for possible_action in possible_actions:
        action_value = find_value(result(board, possible_action))
        if to_play == 'X' and best < action_value:
            best = action_value
            best_action = possible_action
        if to_play == 'O' and best > action_value:
            best = action_value
            best_action = possible_action
    return best_action