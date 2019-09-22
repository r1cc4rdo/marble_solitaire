"""Marble solitaire board explorer.

Usage:
    search_forward BOARD_NAME
    search_forward --help

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
import os
import time
import pickle

from docopt import docopt

from search import initialize_for_board, children, unique_states


def unique_reachable_states(board_name):

    def save_state(index, state):
        with open(f'{board_name}-state-{index:03}.pkl', 'wb') as file_out:
            pickle.dump(state, file_out)

    initial_state = initialize_for_board(board_name)
    states = [{initial_state}]
    save_state(0, states[0])
    while True:

        t_start = time.process_time()
        filename = f'{board_name}-state-{len(states):03}.pkl'
        if os.path.exists(filename):
            with open(filename, 'rb') as file_in:
                states.append(pickle.load(file_in))
                print(f'Moves {len(states) - 1:4}, loaded {len(states[-1]):10} unique states')
                continue

        next_board_ids = children(states[-1])
        if not next_board_ids:  # we are done
            break

        before_dedupe = len(next_board_ids)
        t_search = time.process_time()

        states.append(unique_states(next_board_ids))
        t_dedupe = time.process_time()
        save_state(len(states) - 1, states[-1])

        t_save = time.process_time()
        print(f'Moves {len(states) - 1:4}, states {before_dedupe:10} ({len(states[-1]):10} unique)  '
              f'search/dedupe/save: {t_search - t_start:6.2f} / {t_dedupe - t_search:6.2f} / '
              f'{t_save - t_dedupe:6.2f} seconds')


if __name__ == '__main__':
    args = docopt(__doc__, version='Board explorer v1.0')
    unique_reachable_states(args['BOARD_NAME'])
