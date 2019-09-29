"""Marble solitaire backward search.

Usage:
    search_backward BOARD_NAME BIT_BOARD
"""
import time
import pickle
from pathlib import Path
from docopt import docopt

from search import initialize_for_board, parents, equivalent_boards


def backward_search(board_name, target_position):

    t_start = time.process_time()
    filename = f'{board_name}-boards.pkl'
    with Path(filename).open('rb') as fin:
        bit_boards = pickle.load(fin)
    print(f'Loaded {filename} in {time.process_time() - t_start:.3f} seconds')

    assert target_position in bit_boards[-1]
    bit_boards[-1] = {target_position}
    initialize_for_board(board_name)
    for move in range(len(bit_boards) - 2, 0, -1):

        t_start = time.process_time()

        backward_boards = set()
        parent_boards = parents(bit_boards[move + 1])
        backward_boards.update(parent_boards)
        backward_boards.update(equivalent_boards(parent_boards))
        bit_boards[move].intersection_update(backward_boards)

        print(f'{move:4}: {len(bit_boards[move]):10d}    {time.process_time() - t_start:8.3f}s')

    t_start = time.process_time()
    filename = f'{board_name}-{target_position}.pkl'
    with Path(filename).open('wb') as filename_out:
        pickle.dump(bit_boards, filename_out)
    print(f'Saved {filename} in {time.process_time() - t_start:.3f} seconds')


if __name__ == '__main__':
    args = docopt(__doc__, version='Backward search v1.0')
    backward_search(args['BOARD_NAME'], int(args['BIT_BOARD']))
