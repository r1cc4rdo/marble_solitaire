import numpy as np

from board_io import load_board

powers_of_2 = None  # used as bit masks for each bit in the board representation
board_template = None  # see board_io. -1 on unused grid elements, 0 empty, 1 filled with marble/peg
move_bit_masks = None  # has 1s on the corresponding move representation bits
valid_test_fwd = None  # (bit_state & move_masks) ^ valid_test is 0 iff valid i.e. src, mid, dest == 1, 1, 0
valid_test_bwd = None  # (bit_state & move_masks) ^ valid_test is 0 iff valid i.e. src, mid, dest == 0, 0, 1
shuffle_bit_masks = None  #


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

    :param board_name:
    :return:
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


def int_to_board(bit_state):
    board = np.copy(board_template)
    board[board >= 0] = (bit_state & powers_of_2) > 0
    return board


def parents(bit_states):
    return next_states(bit_states, valid_test_bwd)


def children(bit_states):
    return next_states(bit_states, valid_test_fwd)


def next_states(bit_states, valid_test):
    """
    Return all states reachable from this
    """
    local_move_mask = move_bit_masks

    next_board_ids = set()
    for bit_state in bit_states:
        valid = ((bit_state & local_move_mask) ^ valid_test) == 0
        new_states = bit_state ^ local_move_mask[valid]
        next_board_ids.update(new_states)
    return next_board_ids


def equivalent_states(bit_state, include_self=False):
    """
    Equivalent moves under flip/rotation
    """
    state_bits = (bit_state & powers_of_2) != 0
    shuffle_masks = shuffle_bit_masks[(0 if include_self else 1):]
    return {np.sum(shuffle_mask[state_bits]) for shuffle_mask in shuffle_masks}


def unique_states(bit_states):

    unique_bit_states = set()
    while bit_states:
        state = bit_states.pop()
        unique_bit_states.add(state)
        bit_states -= equivalent_states(state)
    return unique_bit_states
