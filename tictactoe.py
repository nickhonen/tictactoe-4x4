class TicTacToe:
    """
    4x4 TicTacToe/Connect 4 Game

    Valid chars are 'X' and 'O'
    Blank is ' '
    
    """

    @staticmethod
    def generate_board():
        """
        Generates empty 4x4 matrix representing board.
        Empty spaces = ' ' (string with space)

        """
        rows, cols = 4, 4
        return [[' ' for _ in range(cols)] for _ in range(rows)]

    
    def check_winner(self, board):
        """
        Check if there is a winner in the game.
        Winner can be vert, horiz, diag,
        2x2 box, or corners
        
        Uses direction vectors to find pattern from
        each.

        Returns str winning piece or None if no winner

        """
        directions = [
            (0, 1), # horiz
            (1, 0), # vert
            (1, 1), # diag r
            (-1, 1), # diag l
        ]
        
        # checking corners manually
        top_left = board[0][0]
        if top_left == board[0][3] == board[3][0] == board[3][3]:
            return top_left

        # get each position
        for row_idx, row in enumerate(board):
            for col_idx, piece in enumerate(row):
                if piece == ' ':    
                    continue
                
                # get each x and y value of directions, use when there is a piece
                # to find a horiz, diag, or vert line.
                for dx, dy in directions:
                    if self.check_line(board, row_idx, col_idx, dx, dy, piece):
                        return piece
                
                # check 2x2 box, start from valid indexes to
                # avoid index out of bounds
                if row_idx < 3 and col_idx < 3:
                    if self.check_box(board, row_idx, col_idx, piece):
                        return piece
        
        return None


    def check_line(self, board, row, col, dx, dy, piece):
        """
        Helper function, checks next 3 pieces
        in the direction of dx, dy for horiz,
        vert, diag. 

        Returns bool True if line, False if not
        """

        # Avoids index out of bounds for certain values
        if not (0 <= row + (dx * 3) < 4 and
                0 <= col + (dy * 3) < 4):
            return False

        for i in range(1, 4):
            # Gets the next 3 positions of line according to dx, dy
            next_x, next_y = row + (dx * i), col + (dy * i) 
            
            if board[next_x][next_y] != piece:
                return False

        return True

    
    def check_box(self, board, row, col, piece):
        # just checking all pieces in 2x2 box
        # probably didn't need this function, but tried
        # to do it in a different way first
        return (board[row][col] == piece and
                board[row][col+1] == piece and
                board[row+1][col] == piece and
                board[row+1][col+1] == piece)

    
    def any_moves_left(self, board):
        """
        Returns a boolean representing if
        a board has moves left.

        """
        if self.check_winner(board):
            return False

        # if there are any spaces there should be a move left
        return any(' ' in row for row in board)
    
    def is_game_over(self, board):
        """
        Returns a boolean representing if
        the game is over

        """
        return not self.any_moves_left(board)

if __name__ == '__main__':
    game = TicTacToe()
    board_winner = [
        ['X', 'X', 'X', 'X'],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ']
    ]
    print(f'the winner is {game.check_winner(board_winner)}!')