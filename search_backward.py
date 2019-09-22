"""Marble solitaire backward search.

Usage:
    search_backward BOARD_NAME STATE
    search_backward --help

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
import time
import pickle
from pathlib import Path
from docopt import docopt

from search import initialize_for_board, parents, equivalent_states


def load_states(board_name):

    t_start = time.process_time()
    filename = f'{board_name}-states.pkl'
    with Path(filename).open('rb') as fin:
        states = pickle.load(fin)
    print(f'Loaded {filename} in {time.process_time() - t_start:.3f} seconds')
    return states


def save_states(board_name, final_state, states):

    t_start = time.process_time()
    filename = f'{board_name}-{final_state}.pkl'
    with Path(filename).open('wb') as filename_out:
        pickle.dump(states, filename_out)
    print(f'Saved {filename} in {time.process_time() - t_start:.3f} seconds')


def backward_search(board_name, final_state):

    states = load_states(board_name)
    states[-1] = {final_state}
    initialize_for_board(board_name)
    for move in range(len(states) - 2, 0, -1):

        t_start = time.process_time()
        backward_states = set()
        for state in states[move + 1]:

            parent_states = parents(state)
            backward_states.update(parent_states)
            for parent_state in parent_states:
                backward_states.update(equivalent_states(parent_state))

        states[move].intersection_update(backward_states)
        print(f'{move:4}: {len(states[move]):10d}    {time.process_time() - t_start:8.3f}s')

    save_states(board_name, final_state, states)


if __name__ == '__main__':
    args = docopt(__doc__, version='Backward search v1.0')
    backward_search(args['BOARD_NAME'], int(args['STATE']))
