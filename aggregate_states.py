"""Marble solitaire state aggregator.

Usage:
    aggregate_states BOARD_NAME
    aggregate_states --help

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
import time
import pickle
from pathlib import Path
from docopt import docopt

from board_io import print_board
from search import initialize_for_board, int_to_board


def aggregate_states(board_name):

    files = sorted(Path.cwd().glob(f'{board_name}-state-???.pkl'))
    assert(files and (tuple(map(lambda p: int(p.name[-7:-4]), files)) == tuple(range(len(files)))))  # sanity

    states = []
    for filename in files:
        with filename.open('rb') as file_in:
            t_start = time.process_time()
            states.append(pickle.load(file_in))
            print(f'{filename.name} {len(states[-1]):12d} states  {time.process_time() - t_start:8.3f}s')

    t_start = time.process_time()
    filename = f'{board_name}-states.pkl'
    with Path(filename).open('wb') as file_out:
        pickle.dump(states, file_out)
    print(f'Saved {filename} in {time.process_time() - t_start:.3f} seconds')

    for filename in files:
        filename.unlink()

    initialize_for_board(board_name)
    print(f'{len(states[-1])} final unique states for {board_name} board')
    for index, state in enumerate(states[-1]):
        print(f'{index}: {state}')
        print_board(int_to_board(state))


if __name__ == '__main__':
    args = docopt(__doc__, version='State aggregator v1.0')
    aggregate_states(args['BOARD_NAME'])
