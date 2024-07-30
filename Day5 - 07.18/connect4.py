connect_four = []

row1 = [" ", " ", " ", " ", " ", " ", " "]
row2 = [" ", " ", " ", " ", " ", " ", " "]
row3 = [" ", " ", " ", " ", " ", " ", " "]
row4 = [" ", " ", " ", " ", " ", " ", " "]
row5 = [" ", " ", " ", " ", " ", " ", " "]
row6 = [" ", " ", " ", " ", " ", " ", " "]



connect_four.append(row6)
connect_four.append(row5)
connect_four.append(row4)
connect_four.append(row3)
connect_four.append(row2)
connect_four.append(row1)

for row in connect_four:
    print("-----------------------------------")
    print(row)

print("  1 ", "  2 ", "  3 ", "  4 ", "  5 ", "  6 ", "  7 ")



class C4:


    #RED = '\033[91m'
    #BLUE = '\033[96m'
    #RESET = '\033[0m'

    def __init__(self):
        self.active_player = 0
        self.NUM_ROWS = 6
        self.NUM_COLS = 7
        self.game_done = False

        self.connect_four = []
        EMPTY = " "
        self.EMPTY = EMPTY
        row1 = [EMPTY for i in range(self.NUM_COLS)]
        row2 = [EMPTY for i in range(self.NUM_COLS)]
        row3 = [EMPTY for i in range(self.NUM_COLS)]
        row4 = [EMPTY for i in range(self.NUM_COLS)]
        row5 = [EMPTY for i in range(self.NUM_COLS)]
        row6 = [EMPTY for i in range(self.NUM_COLS)]
        row7 = [EMPTY for i in range(self.NUM_COLS)]

        self.connect_four.append(row7)
        self.connect_four.append(row6)
        self.connect_four.append(row5)
        self.connect_four.append(row4)
        self.connect_four.append(row3)
        self.connect_four.append(row2)
        self.connect_four.append(row1)
        self.player1_piece = "X"
        self.player2_piece = "O"



    def add_piece(self, column):
        current_piece = ""

        
        if self.active_player == 0:
            current_piece = self.player1_piece
        else:
            current_piece = self.player2_piece

        for x in range(self.NUM_ROWS, -1, -1):

            if self.connect_four[x][column-1] == self.EMPTY:
                self.connect_four[x][column-1] = current_piece
                break
                

        
        self.active_player = (self.active_player + 1) % 2

        self.print_board()

    def print_board(self):

        for row in self.connect_four:
            print("-----------------------------------")
            print(row)
        print([f"{i}" for i in range(1,self.NUM_COLS+1)])

    def check_if_won_h(self):

        #for i in range(28):
        for r in range(self.NUM_ROWS, -1, -1):
            for y in range(4):
                if self.connect_four[r][y] == self.player1_piece and self.connect_four[r][y+1] == self.player1_piece and self.connect_four[r][y+2] == self.player1_piece and self.connect_four[r][y+3] == self.player1_piece:
                    print("player 1 has won! game is over")
                    self.game_done = True
                    break
                elif self.connect_four[r][y] == self.player2_piece and self.connect_four[r][y+1] == self.player2_piece and self.connect_four[r][y+2] == self.player2_piece and self.connect_four[r][y+3] == self.player2_piece:
                    print("player 2 has won! Game is over")
                    self.game_done = True
                    break
        

    def check_if_won_v(self):
        for r in range(self.NUM_COLS):
            for x in range(5, -1, -1):
                if self.connect_four[x][r] == self.player1_piece and self.connect_four[x-1][r] == self.player1_piece and self.connect_four[x-2][r] == self.player1_piece and self.connect_four[x-3][r] == self.player1_piece:
                    print("player 1 has won! game is over")
                    self.game_done = True
                    break
                elif self.connect_four[x][r] == self.player2_piece and self.connect_four[x-1][r] == self.player2_piece and self.connect_four[x-2][r] == self.player2_piece and self.connect_four[x-3][r] == self.player1_piece:
                    print("player 2 has won! Game is over")
                    self.game_done = True
                    break

    def check_if_won_dL(self):

        counter_x = 0
        counter_y = 0

        for r in range(6):
            for c in range(6):
                if self.connect_four[r][c] == self.player1_piece:
                    counter_x += 1
                    if counter_x == 4:
                        print("Player 1 has won! game is over")
                        self.game_done = True
                        break
                else:
                        counter_x = 0
        
        
        for r in range(6):
            for c in range(6):
                if self.connect_four[r][c] == self.player2_piece:
                    counter_y += 1
                    if counter_y == 4:
                        print("Player 2 has won! game is over")
                        self.game_done = True
                        break
                else:
                        counter_y = 0

      

                
    def check_if_won_dR(self):

        counter_x = 0
        counter_y = 0

        for r in range(6, -1, -1):
            for c in range(6):
                if self.connect_four[r][c] == self.player1_piece:
                    counter_x += 1
                    if counter_x == 4:
                        print("Player 1 has won! game is over")
                        self.game_done = True
                        break
                else:
                        counter_x = 0

        for r in range(6, -1, -1):
            for c in range(6):
                if self.connect_four[r][c] == self.player1_piece:
                    counter_x += 1
                    if counter_x == 4:
                        print("Player 2 has won! game is over")
                        self.game_done = True
                        break
                else:
                        counter_x = 0
        pass




        