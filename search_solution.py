"""Marble solitaire display solution.

Usage:
    sample_solution BOARDS_FILENAME
    sample_solution --help

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
import time
import pickle
import numpy as np
from pathlib import Path
from docopt import docopt

from board_io import load_board
from search import generate_moves_and_shuffles


def search_solution(bit_boards_filename):

    t_start = time.process_time()
    with Path(bit_boards_filename).open('rb') as fin:
        bit_boards = pickle.load(fin)
    print(f'Loaded {bit_boards_filename} in {time.process_time() - t_start:.3f} seconds')

    board_name = bit_boards_filename.split('-')[0]
    initial_board = np.array(load_board(board_name))
    valid_moves, shuffles = generate_moves_and_shuffles(initial_board)
    shuffle_bitmasks = np.power(2, shuffles)
    valid_moves_bitmasks = np.power(2, valid_moves)
    move_masks = np.sum(valid_moves_bitmasks, axis=1)
    valid_test = valid_moves_bitmasks[:, 2]
    powers_of_2 = 2 ** np.arange(len(shuffles[0]))

    for move in reversed(range(len(bit_boards))):

        t_start = time.process_time()
        backward_boards = set()
        for bit_board in bit_boards[move + 1]:

            valid = ((bit_board & move_masks) ^ valid_test) == 0  # find all backward moves
            parent_boards = bit_board ^ move_masks[valid]
            backward_boards.update(parent_boards)

            for parent_board in parent_boards:  # compute their equivalent boards under rotation and flip
                board_bits = (parent_board & powers_of_2) != 0
                dupes = {np.sum(shuffle_bitmask[board_bits]) for shuffle_bitmask in shuffle_bitmasks[1:]}
                backward_boards.update(dupes)

        bit_boards[move].intersection_update(backward_boards)
        print(f'{move:4}: {len(bit_boards[move]):10d}    {time.process_time() - t_start:8.3f}s')


if __name__ == '__main__':
    args = docopt(__doc__, version='Solution sampler v1.0')
    search_solution(args['BOARDS_FILENAME'])
