tic_tac_toe = []

row1 = [" ", " ", " "] 
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

tic_tac_toe.append(row3)
tic_tac_toe.append(row2)
tic_tac_toe.append(row1)

for row in tic_tac_toe:
    print("----------------")
    for i in row:
         print(i, end = " ")


class TTT:   
    def __init__(self):
            self.active_player = 0
            self.NUM_ROWS = 3
            self.NUM_COLS = 3
            self.game_done = False

            self.tic_tac_toe = []
            EMPTY = " "
            self.EMPTY = EMPTY
            row1 = [EMPTY for i in range(self.NUM_COLS)]
            row2 = [EMPTY for i in range(self.NUM_COLS)]
            row3 = [EMPTY for i in range(self.NUM_COLS)]

            self.connect_four.append(row3)
            self.connect_four.append(row2)
            self.connect_four.append(row1)