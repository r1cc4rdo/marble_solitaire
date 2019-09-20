"""Marble solitaire board explorer.

Usage:
    board_explorer BOARD_NAME
    board_explorer --help

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
import os
import time
import pickle

import numpy as np
from docopt import docopt

from board_io import load_board


def unique_reachable_states(board_name):

    def save_state(index, state):
        with open(f'{board_name}-state-{index:03}.pkl', 'wb') as file_out:
            pickle.dump(state, file_out)

    initial_board = np.array(load_board(board_name))
    valid_moves, shuffles = generate_data_structures(initial_board)
    shuffle_bitmasks = np.power(2, shuffles)
    valid_moves_bitmasks = np.power(2, valid_moves)
    move_masks = np.sum(valid_moves_bitmasks, axis=1)  # has 1s on the corresponding move representation bits
    valid_test = np.sum(valid_moves_bitmasks[:, 0:2], axis=1)  # (state & move_masks) ^ valid_test is 0 iff valid (1, 1, 0)
    powers_of_2 = 2 ** np.arange(len(shuffles[0]))

    initial_state = np.sum(powers_of_2 * initial_board[initial_board >= 0])
    states = [{initial_state}]
    save_state(0, states[0])

    while True:

        t_start = time.process_time()
        filename = f'{board_name}-state-{len(states):03}.pkl'
        if os.path.exists(filename):
            with open(filename, 'rb') as file_in:
                states.append(pickle.load(file_in))
                print(f'Moves {len(states) - 1:4}, loaded states      {len(states[-1]):10} unique'
                      f' in {time.process_time() - t_start:6.2f} seconds')
                continue

        next_board_ids = set()
        for state in states[-1]:
            valid = ((state & move_masks) ^ valid_test) == 0
            new_states = state ^ move_masks[valid]
            next_board_ids.update(new_states)

        if not next_board_ids:  # we are done
            break

        before_dedupe = len(next_board_ids)
        t_search = time.process_time()

        unique_states = set()
        while next_board_ids:

            state = next_board_ids.pop()
            state_bits = (state & powers_of_2) != 0
            dupes = {np.sum(shuffle_bitmask[state_bits]) for shuffle_bitmask in shuffle_bitmasks[1:]}
            unique_states.add(state)
            next_board_ids -= dupes

        states.append(unique_states)
        t_dedupe = time.process_time()
        save_state(len(states) - 1, unique_states)

        t_save = time.process_time()
        print(f'Moves {len(states) - 1:4}, states {before_dedupe:10} ({len(states[-1]):10} unique)  '
              f'search/dedupe/save: {t_search - t_start:6.2f} / {t_dedupe - t_search:6.2f} / '
              f'{t_save - t_dedupe:6.2f} seconds')


if __name__ == '__main__':
    args = docopt(__doc__, version='Board explorer v1.0')
    unique_reachable_states(args['BOARD_NAME'])
