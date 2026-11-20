import unittest


def is_passed_pawn(board, i, j):
    """Check whether the pawn at (i, j) is a passed pawn."""
    rows = len(board)
    cols = len(board[0])
    piece = board[i][j]

    if piece == 'P':        # White pawn moves up (row index decreases)
        direction = -1
        enemy = 'p'
    elif piece == 'p':      # Black pawn moves down (row index increases)
        direction = 1
        enemy = 'P'
    else:
        return False        # Not a pawn

    # Check columns j-1, j, j+1 in rows ahead of the pawn
    for c in range(max(0, j - 1), min(cols, j + 2)):
        r = i + direction
        while 0 <= r < rows:
            if board[r][c] == enemy:
                return False
            r += direction
    return True


def passed_pawn(board):
    """Return True only if every pawn on the board is a passed pawn."""
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] in ('p', 'P') and not is_passed_pawn(board, i, j):
                return False

    return True


def make_board(white=None, black=None):
    """Build an 8x8 board from lists of (row, col) coordinates."""
    board = [[' ' for _ in range(8)] for _ in range(8)]
    for r, c in (white or []):
        board[r][c] = 'P'
    for r, c in (black or []):
        board[r][c] = 'p'
    return board


class TestPassedPawn(unittest.TestCase):

    # ---------- Edge cases ----------

    def test_empty_board(self):
        """No pawns on the board -> all (vacuously) passed -> True."""
        board = make_board()
        self.assertTrue(passed_pawn(board))

    def test_single_white_pawn(self):
        """A lone white pawn is always passed."""
        board = make_board(white=[(6, 3)])
        self.assertTrue(passed_pawn(board))

    def test_single_black_pawn(self):
        """A lone black pawn is always passed."""
        board = make_board(black=[(1, 3)])
        self.assertTrue(passed_pawn(board))

    def test_no_pawns_only_pieces(self):
        """Board with no pawns at all -> True."""
        board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] for _ in range(8)]
        self.assertTrue(passed_pawn(board))

    # ---------- Blockade (sample tests) ----------

    def test_blockade_full_rank(self):
        """All black pawns on rank 1, one white pawn on rank 6 -> False."""
        board = make_board(white=[(6, 3)], black=[(1, c) for c in range(8)])
        self.assertFalse(passed_pawn(board))

    def test_blockade_adjacent_column(self):
        """Enemy pawn in an adjacent column ahead blocks the pawn -> False."""
        board = make_board(white=[(6, 3)], black=[(4, 2)])
        self.assertFalse(passed_pawn(board))

    def test_blockade_same_column(self):
        """Enemy pawn in the same column ahead blocks the pawn -> False."""
        board = make_board(white=[(6, 3)], black=[(4, 3)])
        self.assertFalse(passed_pawn(board))

    def test_enemy_pawn_behind_does_not_block(self):
        """Enemy pawn behind the pawn does not make it non-passed -> True."""
        board = make_board(white=[(6, 3)], black=[(7, 2), (7, 3), (7, 4)])
        self.assertTrue(passed_pawn(board))

    def test_enemy_pawn_far_column_does_not_block(self):
        """Enemy pawn two columns away does not block -> True."""
        board = make_board(white=[(6, 3)], black=[(1, 1), (1, 5)])
        self.assertTrue(passed_pawn(board))

    # ---------- Direction of movement ----------

    def test_white_blocked_by_black_ahead(self):
        """White pawn blocked by black pawn ahead -> False."""
        board = make_board(white=[(4, 3)], black=[(2, 3)])
        self.assertFalse(passed_pawn(board))

    def test_black_blocked_by_white_ahead(self):
        """Black pawn blocked by white pawn ahead -> False."""
        board = make_board(black=[(3, 3)], white=[(5, 3)])
        self.assertFalse(passed_pawn(board))

    def test_white_not_blocked_by_black_behind(self):
        """Black pawn behind a white pawn does not block it -> True."""
        board = make_board(white=[(4, 3)], black=[(6, 3)])
        self.assertTrue(passed_pawn(board))

    def test_black_not_blocked_by_white_behind(self):
        """White pawn behind a black pawn does not block it -> True."""
        board = make_board(black=[(3, 3)], white=[(1, 3)])
        self.assertTrue(passed_pawn(board))

    # ---------- Edge columns ----------

    def test_white_pawn_on_left_edge(self):
        """Pawn on column 0 checks only columns 0 and 1 -> True when clear."""
        board = make_board(white=[(6, 0)], black=[(1, 2)])
        self.assertTrue(passed_pawn(board))

    def test_white_pawn_on_left_edge_blocked(self):
        """Pawn on column 0 blocked by enemy in column 1 -> False."""
        board = make_board(white=[(6, 0)], black=[(1, 1)])
        self.assertFalse(passed_pawn(board))

    def test_white_pawn_on_right_edge(self):
        """Pawn on column 7 checks only columns 6 and 7 -> True when clear."""
        board = make_board(white=[(6, 7)], black=[(1, 5)])
        self.assertTrue(passed_pawn(board))

    def test_white_pawn_on_right_edge_blocked(self):
        """Pawn on column 7 blocked by enemy in column 6 -> False."""
        board = make_board(white=[(6, 7)], black=[(1, 6)])
        self.assertFalse(passed_pawn(board))

    # ---------- Multiple pawns ----------

    def test_all_pawns_passed(self):
        """Several pawns, none blocked -> True."""
        board = make_board(white=[(6, 0), (6, 7)], black=[(1, 3), (1, 4)])
        self.assertTrue(passed_pawn(board))

    def test_one_of_many_blocked(self):
        """One blocked pawn among many is enough -> False."""
        board = make_board(
            white=[(6, 0), (6, 3), (6, 7)],
            black=[(1, 2)],   # blocks the white pawn at (6, 3)
        )
        self.assertFalse(passed_pawn(board))

    def test_friendly_pawn_does_not_block(self):
        """A friendly pawn ahead does not make a pawn non-passed -> True."""
        board = make_board(white=[(4, 3), (3, 3)])
        self.assertTrue(passed_pawn(board))

    # ---------- is_passed_pawn unit tests ----------

    def test_is_passed_pawn_non_pawn_square(self):
        """Empty square -> is_passed_pawn returns False."""
        board = make_board()
        self.assertFalse(is_passed_pawn(board, 4, 4))

    def test_is_passed_pawn_white_clear(self):
        """White pawn with clear path -> True."""
        board = make_board(white=[(4, 3)])
        self.assertTrue(is_passed_pawn(board, 4, 3))

    def test_is_passed_pawn_white_blocked(self):
        """White pawn blocked by black pawn -> False."""
        board = make_board(white=[(4, 3)], black=[(2, 4)])
        self.assertFalse(is_passed_pawn(board, 4, 3))

    def test_is_passed_pawn_black_clear(self):
        """Black pawn with clear path -> True."""
        board = make_board(black=[(3, 3)])
        self.assertTrue(is_passed_pawn(board, 3, 3))

    def test_is_passed_pawn_black_blocked(self):
        """Black pawn blocked by white pawn -> False."""
        board = make_board(black=[(3, 3)], white=[(5, 2)])
        self.assertFalse(is_passed_pawn(board, 3, 3))

    def test_is_passed_pawn_pawn_on_first_rank_white(self):
        """White pawn on rank 0 (already promoted square) -> no rows ahead -> True."""
        board = make_board(white=[(0, 3)], black=[(1, 2)])
        self.assertTrue(is_passed_pawn(board, 0, 3))

    def test_is_passed_pawn_pawn_on_last_rank_black(self):
        """Black pawn on rank 7 -> no rows ahead -> True."""
        board = make_board(black=[(7, 3)], white=[(6, 2)])
        self.assertTrue(is_passed_pawn(board, 7, 3))


if __name__ == '__main__':
    unittest.main()