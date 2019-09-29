import numpy as np

from board_io import load_board

powers_of_2 = None  # used as bit masks for each bit in the board representation
board_template = None  # see board_io. -1 on unused grid elements, 0 empty, 1 filled with marble/peg
move_bit_masks = None  # has 1s on the corresponding move representation bits
valid_test_fwd = None  # (bit_board & move_masks) ^ valid_test is 0 iff valid i.e. src, mid, dest == 1, 1, 0
valid_test_bwd = None  # (bit_board & move_masks) ^ valid_test is 0 iff valid i.e. src, mid, dest == 0, 0, 1
shuffle_bit_masks = None  # powers_of_2 * (bit_board & shuffle_mask != 0) is an rotation/reflection equivalent board


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


def initialize_for_board(board_name):
    """
    Initializes global variables powers_of_2, board_template, move_bit_masks, valid_test_fwd, valid_test_bwd and
    shuffle_bit_masks for a given board type. The variables are shared across all functions in this module.
    See the comments at their declaration site for a detailed description of each.
    """
    global powers_of_2, board_template, move_bit_masks, valid_test_fwd, valid_test_bwd, shuffle_bit_masks

    board_template = np.array(load_board(board_name))
    valid_moves, shuffles = generate_moves_and_shuffles(board_template)

    valid_moves_bitmasks = np.power(2, valid_moves)
    move_bit_masks = np.sum(valid_moves_bitmasks, axis=1)
    valid_test_fwd = np.sum(valid_moves_bitmasks[:, 0:2], axis=1)
    valid_test_bwd = valid_moves_bitmasks[:, 2]

    shuffle_bit_masks = np.power(2, shuffles)
    powers_of_2 = 2 ** np.arange(len(shuffles[0]))

    return board_to_int(board_template)


def board_to_int(board):
    return np.sum(powers_of_2[board[board >= 0] > 0])


def int_to_board(bit_board):
    board = np.copy(board_template)
    board[board >= 0] = (bit_board & powers_of_2) > 0
    return board


def parents(bit_boards):
    return next_boards(bit_boards, valid_test_bwd)


def children(bit_boards):
    return next_boards(bit_boards, valid_test_fwd)


def next_boards(bit_boards, valid_test):
    """
    Computes the board configurations that can be reached through valid forward and backward moves.
    A forward move is the standard jump to remove mechanic; backward is the opposite process.
    """
    local_move_mask = move_bit_masks
    all_next_boards = set()
    for bit_board in bit_boards:
        valid = ((bit_board & local_move_mask) ^ valid_test) == 0
        next_bit_boards = bit_board ^ local_move_mask[valid]
        all_next_boards.update(next_bit_boards)
    return all_next_boards


def equivalent_boards(bit_boards):

    if not isinstance(bit_boards, set):
        bit_boards = {bit_boards}
    boards_bits = ((bit_board & powers_of_2) != 0 for bit_board in bit_boards)
    return {np.sum(shuffle_mask[board_bits]) for board_bits in boards_bits for shuffle_mask in shuffle_bit_masks[1:]}


def unique_boards(bit_boards):

    unique_bit_boards = set()
    while bit_boards:
        bit_board = bit_boards.pop()
        unique_bit_boards.add(bit_board)
        bit_boards -= equivalent_boards(bit_board)
    return unique_bit_boards
