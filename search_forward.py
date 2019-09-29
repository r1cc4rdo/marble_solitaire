"""Marble solitaire board explorer.

Usage:
    forward_search BOARD_NAME
    forward_search --help

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
import time
import pickle
from pathlib import Path

from docopt import docopt

from search import initialize_for_board, children, unique_boards, int_to_board
from board_io import print_board


def checkpoint():
    curr = 0
    while True:
        prev, curr = curr, time.process_time()
        yield curr - prev


def forward_search(board_name):

    def save_state(index, state):
        with Path(f'{board_name}-state-{index:03}.pkl').open('wb') as file_out:
            pickle.dump(state, file_out)

    initial_state = initialize_for_board(board_name)
    states = [{initial_state}]
    save_state(0, states[0])
    partial_state_files = []
    while True:

        checkpoint()  # reset timer

        filename = Path(f'{board_name}-state-{len(states):03}.pkl')
        partial_state_files.append(filename)
        if filename.exists():
            with filename.open('rb') as file_in:
                states.append(pickle.load(file_in))
                print(f'Moves {len(states) - 1:4}, loaded {len(states[-1]):10} unique states')
                continue

        next_board_ids = children(states[-1])
        if not next_board_ids:  # we are done
            break

        before_dedupe = len(next_board_ids)
        t_search = checkpoint()

        states.append(unique_boards(next_board_ids))
        t_dedupe = checkpoint()
        save_state(len(states) - 1, states[-1])

        t_save = checkpoint()
        print(f'Moves {len(states) - 1:4}, states {before_dedupe:10} ({len(states[-1]):10} unique)  '
              f'search/dedupe/save: {t_search:6.2f} / {t_dedupe:6.2f} / {t_save:6.2f} seconds')

    print('Saving states...')
    t_start = time.process_time()
    filename = f'{board_name}-states.pkl'
    with Path(filename).open('wb') as file_out:
        pickle.dump(states, file_out)
    print(f'Saved {filename} in {time.process_time() - t_start:.3f} seconds')

    for filename in partial_state_files:
        filename.unlink()

    initialize_for_board(board_name)
    print(f'{len(states[-1])} final unique states for {board_name} board')
    for index, state in enumerate(states[-1]):
        print(f'{index}: {state}')
        print_board(int_to_board(state))


if __name__ == '__main__':
    args = docopt(__doc__, version='Board explorer v1.0')
    forward_search(args['BOARD_NAME'])
