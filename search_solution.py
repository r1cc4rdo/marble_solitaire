"""Marble solitaire display solution.

Usage:
    search_solution BOARD_NAME BIT_BOARD
"""
import pickle
from pathlib import Path
from docopt import docopt
from copy import copy

from search import initialize_for_board, children, equivalent_boards, int_to_board
from board_io import print_board


def search_solution(board_name, target_position):

    initialize_for_board(board_name)

    print('Loading boards...')
    filename = f'{board_name}-{target_position}.pkl'
    with Path(filename).open('rb') as fin:
        bit_boards = pickle.load(fin)

    board_sequence = []
    next_moves = copy(bit_boards[0])
    for all_valid_positions in bit_boards[1:]:

        next_move = next_moves.pop()  # choose any, all are valid!
        board_sequence.append(next_move)

        reachable_boards = children((next_move, ))  # positions that can be reached from chosen
        move_candidates = equivalent_boards(reachable_boards).intersection(all_valid_positions)
        next_moves = reachable_boards.intersection(equivalent_boards(move_candidates))

    board_sequence.append(next_moves.pop())
    for index, bit_board in enumerate(board_sequence):
        print(f'Move {index:2d} {"-" * 5}')
        print_board(int_to_board(bit_board))


if __name__ == '__main__':
    args = docopt(__doc__, version='Solution sampler v1.0')
    search_solution(args['BOARD_NAME'], args['BIT_BOARD'])
