"""Marble solitaire backward search.

Usage:
    backward_search BOARD_NAME STATE
    backward_search --help

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
from boards_explorer import generate_data_structures


def backward_search(board_name, final_state):

    t_start = time.process_time()
    filename = f'{board_name}-states.pkl'
    with Path(filename).open('rb') as fin:
        states = pickle.load(fin)
    print(f'Loaded {filename} in {time.process_time() - t_start:.3f} seconds')

    initial_board = np.array(load_board(board_name))
    valid_moves, shuffles = generate_data_structures(initial_board)
    shuffle_bitmasks = np.power(2, shuffles)
    valid_moves_bitmasks = np.power(2, valid_moves)
    move_masks = np.sum(valid_moves_bitmasks, axis=1)  # has 1s on the corresponding move representation bits
    valid_test = valid_moves_bitmasks[:, 2]  # (state & move_masks) ^ valid_test is 0 iff valid (0, 0, 1)
    powers_of_2 = 2 ** np.arange(len(shuffles[0]))

    states[-1] = {final_state}
    for move in range(len(states) - 2, 0, -1):

        t_start = time.process_time()
        backward_states = set()
        for state in states[move + 1]:

            valid = ((state & move_masks) ^ valid_test) == 0  # find all backward moves
            parent_states = state ^ move_masks[valid]
            backward_states.update(parent_states)

            for parent_state in parent_states:  # compute their equivalent state under rotation and flip
                state_bits = (parent_state & powers_of_2) != 0
                dupes = {np.sum(shuffle_bitmask[state_bits]) for shuffle_bitmask in shuffle_bitmasks[1:]}
                backward_states.update(dupes)

        states[move].intersection_update(backward_states)
        print(f'{move:4}: {len(states[move]):10d}    {time.process_time() - t_start:8.3f}s')

    t_start = time.process_time()
    filename = f'{board_name}-{final_state}.pkl'
    with Path(filename).open('wb') as filename_out:
        pickle.dump(states, filename_out)
    print(f'Saved {filename} in {time.process_time() - t_start:.3f} seconds')


if __name__ == '__main__':
    args = docopt(__doc__, version='Backward search v1.0')
    backward_search(args['BOARD_NAME'], int(args['STATE']))
