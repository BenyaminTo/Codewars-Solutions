def check_move_validity(piece, starting_square, ending_square):
    # Convert e.g. "e4" to zero-based (file, rank) = (4, 3)
    start = (ord(starting_square[0].lower()) - ord('a'), int(starting_square[1]) - 1)
    end = (ord(ending_square[0].lower()) - ord('a'), int(ending_square[1]) - 1)
    x, y = start

    piece_moves = []

    ###########################################################################
    if piece == 'K' or piece == 'k':
        # One square in each of the 8 directions
        piece_moves.append((x + 1, y))
        piece_moves.append((x + 1, y - 1))
        piece_moves.append((x, y - 1))
        piece_moves.append((x - 1, y - 1))
        piece_moves.append((x - 1, y))
        piece_moves.append((x - 1, y + 1))
        piece_moves.append((x, y + 1))
        piece_moves.append((x + 1, y + 1))

    ###########################################################################
    elif piece == 'Q' or piece == 'q':
        # Diagonal lines until the edge of the board
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                piece_moves.append((nx, ny))
                nx += dx
                ny += dy

        # The whole file and the whole rank
        for i in range(8):
            piece_moves.append((x, i))
            piece_moves.append((i, y))

    ###########################################################################
    elif piece == 'R' or piece == 'r':
        # The whole file and the whole rank
        for i in range(8):
            piece_moves.append((x, i))
            piece_moves.append((i, y))

    ###########################################################################
    elif piece == 'B' or piece == 'b':
        # Diagonal lines until the edge of the board
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                piece_moves.append((nx, ny))
                nx += dx
                ny += dy

    ###########################################################################
    elif piece == 'N' or piece == 'n':
        # The 8 L-shaped jumps
        piece_moves.append((x + 1, y + 2))
        piece_moves.append((x + 2, y + 1))
        piece_moves.append((x + 1, y - 2))
        piece_moves.append((x + 2, y - 1))
        piece_moves.append((x - 2, y - 1))
        piece_moves.append((x - 1, y - 2))
        piece_moves.append((x - 2, y + 1))
        piece_moves.append((x - 1, y + 2))

    ###########################################################################
    elif piece == 'P':
        # White pawn: cannot start on rank 1 (index 0)
        if y >= 1:
            piece_moves.append((x, y + 1))
            # Two squares forward only from the starting rank 2 (index 1)
            if y == 1:
                piece_moves.append((x, y + 2))

    ###########################################################################
    elif piece == 'p':
        # Black pawn: cannot start on rank 8 (index 7)
        if y <= 6:
            piece_moves.append((x, y - 1))
            # Two squares forward only from the starting rank 7 (index 6)
            if y == 6:
                piece_moves.append((x, y - 2))

    ###########################################################################
    else:
        return False

    # Keep only squares that are on the board and different from the start square
    piece_moves = [m for m in piece_moves
                   if 0 <= m[0] <= 7 and 0 <= m[1] <= 7 and m != start]

    return end in piece_moves
###############################################################################
import unittest

# from solution import check_move_validity   # uncomment if the function is in another file


class TestCheckMoveValidity(unittest.TestCase):

    def run_cases(self, cases):
        # Each case is (piece, start, end, expected_result)
        for piece, start, end, expected in cases:
            with self.subTest(piece=piece, start=start, end=end):
                self.assertEqual(check_move_validity(piece, start, end), expected)

    def test_king(self):
        self.run_cases([
            ("K", "e4", "e5", True),    # one square up
            ("K", "e4", "f5", True),    # one square diagonally
            ("K", "e4", "d3", True),
            ("k", "h8", "g7", True),    # black king in a corner
            ("K", "e4", "e6", False),   # two squares
            ("K", "e4", "g4", False),
            ("K", "e4", "f6", False),   # knight-like jump
            ("K", "a1", "a1", False),   # same square
        ])

    def test_queen(self):
        self.run_cases([
            ("Q", "d1", "d8", True),    # along the file
            ("Q", "d1", "a1", True),    # along the rank
            ("Q", "d1", "h5", True),    # diagonal
            ("q", "a1", "h8", True),    # long diagonal, black queen
            ("Q", "d1", "e3", False),   # knight-like jump
            ("Q", "d1", "f5", False),
            ("Q", "d4", "d4", False),   # same square
        ])

    def test_rook(self):
        self.run_cases([
            ("R", "a1", "a8", True),
            ("R", "a1", "h1", True),
            ("r", "h8", "h1", True),
            ("R", "d4", "d5", True),
            ("R", "a1", "b2", False),   # diagonal
            ("R", "a1", "b3", False),
            ("R", "d4", "d4", False),   # same square
        ])

    def test_bishop(self):
        self.run_cases([
            ("B", "c1", "h6", True),
            ("B", "c1", "a3", True),
            ("b", "f8", "a3", True),    # black bishop
            ("B", "e4", "f5", True),
            ("B", "c1", "c4", False),   # straight line
            ("B", "c1", "d1", False),
            ("B", "e4", "e4", False),   # same square
        ])

    def test_knight(self):
        self.run_cases([
            ("N", "g1", "f3", True),
            ("N", "g1", "h3", True),
            ("N", "g1", "e2", True),
            ("n", "b8", "c6", True),    # black knight
            ("N", "a1", "b3", True),    # corner
            ("N", "g1", "g3", False),   # straight line
            ("N", "a1", "c3", False),   # diagonal
            ("N", "e4", "e4", False),   # same square
        ])

    def test_white_pawn(self):
        self.run_cases([
            ("P", "e2", "e3", True),    # one step from the starting rank
            ("P", "e2", "e4", True),    # two steps from the starting rank
            ("P", "e3", "e4", True),    # one step elsewhere
            ("P", "e7", "e8", True),    # last step to rank 8
            ("P", "e3", "e5", False),   # two steps not from the starting rank
            ("P", "e2", "e5", False),   # three steps
            ("P", "e4", "e3", False),   # backwards
            ("P", "e2", "e1", False),   # backwards
            ("P", "e2", "d3", False),   # diagonal (captures are ignored)
            ("P", "e2", "f3", False),
            ("P", "e2", "d2", False),   # sideways
            ("P", "e2", "e2", False),   # same square
            ("P", "e1", "e2", False),   # cannot start before the starting rank
            ("P", "e1", "e3", False),
            ("P", "e8", "e7", False),
        ])

    def test_black_pawn(self):
        self.run_cases([
            ("p", "e7", "e6", True),
            ("p", "e7", "e5", True),
            ("p", "e6", "e5", True),
            ("p", "e2", "e1", True),    # last step to rank 1
            ("p", "e6", "e4", False),   # two steps not from the starting rank
            ("p", "e5", "e6", False),   # backwards
            ("p", "e7", "e8", False),   # backwards
            ("p", "e7", "d6", False),   # diagonal
            ("p", "e7", "e7", False),   # same square
            ("p", "e8", "e7", False),   # cannot start before the starting rank
            ("p", "e8", "e6", False),
            ("p", "e1", "e2", False),
        ])

    def test_unknown_piece(self):
        self.run_cases([
            ("X", "e4", "e5", False),
        ])

    def test_uppercase_squares(self):
        # Squares given in uppercase should not crash
        self.run_cases([
            ("N", "G1", "F3", True),
        ])

    def test_move_counts(self):
        # Count how many destination squares are valid from a given square
        files = "abcdefgh"
        ranks = "12345678"
        squares = [f + r for f in files for r in ranks]

        def count(piece, start):
            return sum(check_move_validity(piece, start, end) for end in squares)

        # From the centre square d4
        self.assertEqual(count("K", "d4"), 8)
        self.assertEqual(count("Q", "d4"), 27)
        self.assertEqual(count("R", "d4"), 14)
        self.assertEqual(count("B", "d4"), 13)
        self.assertEqual(count("N", "d4"), 8)

        # From the corner a1
        self.assertEqual(count("K", "a1"), 3)
        self.assertEqual(count("Q", "a1"), 21)
        self.assertEqual(count("R", "a1"), 14)
        self.assertEqual(count("B", "a1"), 7)
        self.assertEqual(count("N", "a1"), 2)

        # Pawns
        self.assertEqual(count("P", "e2"), 2)
        self.assertEqual(count("P", "e3"), 1)
        self.assertEqual(count("P", "e1"), 0)
        self.assertEqual(count("p", "e7"), 2)
        self.assertEqual(count("p", "e6"), 1)
        self.assertEqual(count("p", "e8"), 0)


if __name__ == "__main__":
    unittest.main()