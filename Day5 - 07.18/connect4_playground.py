from connect4 import C4


game = C4()


while game.game_done == False:
    player_input = int(input("Please choose a column to place piece in: "))
    game.add_piece(player_input)
    game.check_if_won_h()
    game.check_if_won_v()
    game.check_if_won_dL()




