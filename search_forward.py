"""Marble solitaire forward search.

Usage:
    search_forward BOARD_NAME
"""
import time
import pickle
from pathlib import Path

from docopt import docopt

from search import initialize_for_board, children, unique_boards, int_to_board
from board_io import print_board


def forward_search(board_name):

    def save_bit_boards(index, bit_boards):
        with Path(filename_format.format(board_name, index)).open('wb') as file_out:
            pickle.dump(bit_boards, file_out)

    filename_format = '{}-board-{:03d}.pkl'
    starting_position = initialize_for_board(board_name)
    boards_at_move = [{starting_position}]
    save_bit_boards(0, boards_at_move[0])
    while True:

        filename = Path(filename_format.format(board_name, len(boards_at_move)))
        if filename.exists():
            with filename.open('rb') as file_in:
                boards_at_move.append(pickle.load(file_in))
                print(f'Moves {len(boards_at_move) - 1:4}, loaded {len(boards_at_move[-1]):10} unique boards')
                continue

        t_start = time.process_time()
        next_board_ids = children(boards_at_move[-1])
        board_count = len(next_board_ids)
        t_search = time.process_time()

        if not next_board_ids:  # we are done
            break

        boards_at_move.append(unique_boards(next_board_ids))
        t_dedupe = time.process_time()

        save_bit_boards(len(boards_at_move) - 1, boards_at_move[-1])
        t_save = time.process_time()

        t_search, t_dedupe, t_save = t_search - t_start, t_dedupe - t_search, t_save - t_dedupe
        print(f'Moves {len(boards_at_move) - 1:4}, boards {board_count:10} ({len(boards_at_move[-1]):10} unique)  '
              f'search/dedupe/save: {t_search:6.2f} / {t_dedupe:6.2f} / {t_save:6.2f} seconds')

    print('Saving boards...')
    t_start = time.process_time()
    filename = f'{board_name}-boards.pkl'
    with Path(filename).open('wb') as file_out:
        pickle.dump(boards_at_move, file_out)
    print(f'Saved {filename} in {time.process_time() - t_start:.3f} seconds')

    for index in range(len(boards_at_move)):
        Path(filename_format.format(board_name, index)).unlink()

    print(f'{len(boards_at_move[-1])} final unique boards for {board_name} board')
    for index, board in enumerate(boards_at_move[-1]):
        print(f'#{index} [{board}]')
        print_board(int_to_board(board))


if __name__ == '__main__':
    args = docopt(__doc__, version='Board explorer v1.0')
    forward_search(args['BOARD_NAME'])
