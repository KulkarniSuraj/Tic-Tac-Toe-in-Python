# dependencies 
import itertools
from GameBoard import game_board, create_game
from WinGame import win

# main function
play = True
players = [1, 2] # list of players

while play:

	game_size = int(input("What size of tic-tac-toe do you want to play? : "))
	game = create_game(game_size)
	game_won = False
	game, _ = game_board(game, just_display = True)
	player_choice = itertools.cycle(players)	
	while not game_won:
		current_player = next(player_choice)
		print(f"Current player : {current_player}")	
		played = False
		# this loop will continue until successful play
		while not played:
			# taking row and column position from player to play 
			row_choice = int(input("What row do you want to play ? (0, 1, 2) : "))
			column_choice = int(input("What column do you want to play ? (0, 1, 2) : "))
			game, played = game_board(game, current_player, row_choice, column_choice)
		
		if win(game):
			game_won = True
			again = input("Do you want to play again (y/n) ? : ")
			
			if again.lower() == 'y':
				print("restarting.....\n")
			elif again.lower() == 'n':
				print("Bye ")
				play = False
			else:
				print("invalid input. see you soon")
				play = False