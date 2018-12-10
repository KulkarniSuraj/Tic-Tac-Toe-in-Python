# dependencies
from colorama import init, Fore, Style, deinit



def game_board(game_map, player = 1, row = 0, column = 0, just_display = False):

	if game_map[row][column] != 0:
		print("This position is occupied. Choose another one")
		return game_map, False

	try:
		if not just_display:
			game_map[row][column] = player

		# printing the game board	
		col_string = ' '
		for i in range(len(game_map)):
			col_string += "  " + str(i)
		print(col_string) # print the column numbers
		init()
		# enumerate returns index and iterable in the form of tuple
		for row_number, row in enumerate(game_map):
			#print(row_number, row)
			symbol_string = ""
			for item in row:
				if item == 0:
					symbol_string += "   "
				elif item == 1:
					symbol_string += Fore.RED + " X " + Style.RESET_ALL
				else:
					symbol_string += Fore.GREEN + " O " + Style.RESET_ALL
			print(row_number, symbol_string)
		deinit()	
		print("\n") # a line left blank below game board to display it properly
		return game_map, True
	except IndexError as e:
		print("Please make sure you entered correct values 0, 1, 2. |", e)
		return game_map, False
	except Exception as e:
		print("Something went wrong!", e)
		return game_map, False



def create_game(game_size):
	game = []
	for row in range(game_size):
		row = [] # creating a row
		for i in range(game_size):
			row.append(0) # adding 0's to row

		game.append(row) # appending row of 0's to game 

	return game