encoding = {

    'numbers': (0, 1, -1),
    'ascii': ('O', '*', '.'),
    'unicode': tuple(chr(uc) for uc in (9898, 9899, 11036)),  # white circle, black circle, white square
    'labels': ('empty', 'marble', 'placeholder')}

boards = {  # ascii encoded

    'british': """
                . . * * * . .
                . . * * * . .
                * * * * * * *
                * * * O * * *
                * * * * * * *
                . . * * * . .
                . . * * * . .
                """,

    'european': """
                . . * * * . .
                . * * * * * .
                * * * * * * *
                * * * O * * *
                * * * * * * *
                . * * * * * .
                . . * * * . .
                """,

    'japanese': """
                . . . * * * . . .
                . . . * * * . . .
                . . . * * * . . .
                * * * * * * * * *
                * * * * O * * * *
                * * * * * * * * *
                . . . * * * . . .
                . . . * * * . . .
                . . . * * * . . .
                """}


def load_board(name):
    """
    Loads a board's initial configurations.
    Example:

    >>> load_board('british')[::3]
    [[-1, -1, 1, 1, 1, -1, -1], [1, 1, 1, 0, 1, 1, 1], [-1, -1, 1, 1, 1, -1, -1]]

    :param name: board to load, either 'british', 'european' or 'japanese'
    :return: list of rows, with 0/1 representing empty/filled spaces and -1 unused ones
    """
    ascii_to_numbers = dict(zip(encoding['ascii'], encoding['numbers']))
    rows_string = (s.replace(' ', '') for s in boards[name].split('\n') if s.strip())
    return [[ascii_to_numbers[symbol] for symbol in row] for row in rows_string]


def print_board(board, encoding_format='ascii'):
    """
    >>> print_board(load_board('british'))
    . . * * * . .
    . . * * * . .
    * * * * * * *
    * * * O * * *
    * * * * * * *
    . . * * * . .
    . . * * * . .
    """
    numbers_to_encoding = dict(zip(encoding['numbers'], encoding[encoding_format]))
    print('\n'.join(' '.join(numbers_to_encoding[value] for value in row) for row in board))


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
