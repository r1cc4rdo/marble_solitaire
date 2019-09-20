import numpy as np

from board_io import load_board

board_template = None  #
valid_moves = None  #
shuffles = None  #
shuffle_bitmasks = None  #
valid_moves_bitmasks = None  #
move_masks = None  #
valid_test_fwd = None  #
valid_test_bwd = None  #
powers_of_2 = None  #


def generate_moves_and_shuffles(template):
    """
    Given an initial board representation, returns the list of valid moves' indexes and the permutations
    required to generate equivalent board positions (equivalent up to an arbitrary rotation and flip).
    Valid moves are returned as list of triples of indexes in the bit representation of the board, specifying
    respectively the index of the starting, intermediate and final location of a move.
    """
    bit_index = template.copy()
    valid_rc = np.argwhere(bit_index >= 0)
    bit_index[valid_rc[:, 0], valid_rc[:, 1]] = np.arange(len(valid_rc))  # from location to corresponding bit index

    valid_moves = []  # list of (start, intermediate, end) indexes
    for displacement in ((0, -2), (-2, 0), (0, 2), (2, 0)):  # left, up, right, down
        for source, destination in zip(valid_rc, valid_rc + displacement):
            if destination.tolist() in valid_rc.tolist():  # tolist() to disable broadcasting
                (sr, sc), (ir, ic), (dr, dc) = source, (source + destination) // 2, destination
                valid_moves.append((bit_index[sr, sc], bit_index[ir, ic], bit_index[dr, dc]))

    shuffles = []  # permutations to obtain equivalent boards
    flipped_index = np.fliplr(bit_index)  # mirrored
    for _ in range(4):  # rotated 0, 90, 180, 270 degrees
        shuffles.extend((bit_index, flipped_index))
        bit_index, flipped_index = map(np.rot90, (bit_index, flipped_index))

    return valid_moves, tuple(tuple(s[s >= 0]) for s in shuffles)


def initialize(board_name):
    """

    :param board_name:
    :return:
    """

    initial_board = np.array(load_board(board_name))
    valid_moves, shuffles = generate_data_structures(initial_board)
    shuffle_bitmasks = np.power(2, shuffles)
    valid_moves_bitmasks = np.power(2, valid_moves)
    move_masks = np.sum(valid_moves_bitmasks, axis=1)  # has 1s on the corresponding move representation bits
    valid_test = np.sum(valid_moves_bitmasks[:, 0:2],
                        axis=1)  # (state & move_masks) ^ valid_test is 0 iff valid (1, 1, 0)
    powers_of_2 = 2 ** np.arange(len(shuffles[0]))
