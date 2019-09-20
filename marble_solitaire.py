import numpy as np
from itertools import product
from functools import lru_cache


options = {
    'goal': 5,  # stop when a solution with {goal} beads is found
    'cache_power': 11}  # lru_cache.maxsize == 2 ** cache_power


def board_mask():
    board = np.zeros((13, 13))
    board[5:8, 2:11] = 1
    board[2:11, 5:8] = 1
    return board == 1


def bool_tuple_to_board(bt):
    board = -np.ones((13, 13))
    board[mask] = bt
    return board


def board_to_bool_tuple(board):
    return tuple(board[mask] == 1)


def print_board(board):
    chars = {-1: '⬜', 1: '⚫', 0: '⚪'}
    print('\n'.join(' '.join(chars[value] for value in row[2:-2]) for row in board[2:-2]))


def generate_moves(bt):
    board = bool_tuple_to_board(bt)
    empty_spaces = np.argwhere(board == 0)
    displacements = ((-1, 0), (0, -1), (1, 0), (0, 1))
    for (r, c), (dr, dc) in product(empty_spaces, displacements):

        to_be_removed_coord = r + dr, c + dc  # coordinate of the bead being jumped over
        if not board[to_be_removed_coord] == 1:  # skip if empty or out of bounds
            continue

        jumping_bead_coord = r + 2 * dr, c + 2 * dc  # coordinate of the bead which is jumping
        if not board[jumping_bead_coord] == 1:  # skip if empty or out of bounds
            continue

        new_board = np.array(board)
        new_board[to_be_removed_coord] = 0
        new_board[jumping_bead_coord] = 0
        new_board[r, c] = 1

        yield board_to_bool_tuple(new_board), (r, c, dr, dc)


@lru_cache(maxsize=2**options['cache_power'])
def solve(bool_tuple):
    for next_board, move in generate_moves(bool_tuple):
        if solve(next_board):
            print(move)
            return True
    return sum(bool_tuple) <= options['goal']


if __name__ == '__main__':

    mask = board_mask()
    initial_configuration = (True, ) * 22 + (False, ) + (True, ) * 22
    print_board(bool_tuple_to_board(initial_configuration))
    solve(initial_configuration)
