class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'
        self.moves_left = 42  # Total number of cells in the board

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
        print('+---+---+---+---+---+---+---+')
        print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 |')
        print('+---+---+---+---+---+---+---+')

    def drop_piece(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                self.moves_left -= 1
                return True
        return False

    def check_win(self):
        # Check horizontal
        for row in range(6):
            for col in range(4):
                if (self.board[row][col] == self.current_player and
                    self.board[row][col+1] == self.current_player and
                    self.board[row][col+2] == self.current_player and
                    self.board[row][col+3] == self.current_player):
                    return True

        # Check vertical
        for col in range(7):
            for row in range(3):
                if (self.board[row][col] == self.current_player and
                    self.board[row+1][col] == self.current_player and
                    self.board[row+2][col] == self.current_player and
                    self.board[row+3][col] == self.current_player):
                    return True

        # Check positively sloped diagonals
        for row in range(3):
            for col in range(4):
                if (self.board[row][col] == self.current_player and
                    self.board[row+1][col+1] == self.current_player and
                    self.board[row+2][col+2] == self.current_player and
                    self.board[row+3][col+3] == self.current_player):
                    return True

        # Check negatively sloped diagonals
        for row in range(3):
            for col in range(3, 7):
                if (self.board[row][col] == self.current_player and
                    self.board[row+1][col-1] == self.current_player and
                    self.board[row+2][col-2] == self.current_player and
                    self.board[row+3][col-3] == self.current_player):
                    return True

        return False

    def play_game(self):
        while True:
            self.print_board()

            if self.moves_left == 0:
                print("It's a draw!")
                break

            column = int(input(f"Player {self.current_player}, enter column (1-7): ")) - 1

            if column < 0 or column > 6:
                print("Invalid column number. Please choose between 1 and 7.")
                continue

            if not self.drop_piece(column):
                print("Column is full. Please choose another column.")
                continue

            if self.check_win():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            # Switch turns
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'

if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()
