def win(current_game):
	def are_all_same(l):
		''' This function checks whether all elements of lists are identical or not'''
		if l[0] != 0 and l.count(l[0]) == len(l):
			return True
		else:
			return False


	# horizontal win
	for row in current_game:
		#print(row)
		if are_all_same(row):
			print(f"Hurrah! player {row[0]} is the winner horizontally (-)!")
			return True


	# vertical win
	for col in range(len(current_game)):
		check = []

		for row in current_game:
			check.append(row[col])

		if are_all_same(check):
			print(f"Hurrah! player {check[0]} is the winner vertically (|)!")
			return True

	# diagonal win
	diags1 = []

	# testing other diagonal
	for col, row in enumerate(reversed(range(len(current_game)))):
		diags1.append(current_game[row][col])
	if are_all_same(diags1):
		print(f"Hurrah! player {diags1[0]} is the winner diagonally (/)!")
		return True

	# testing for main diagonal
	diags2 = []
	for i in range(len(current_game)):
		diags2.append(current_game[i][i])

	if are_all_same(diags2):
		print(f"Hurrah! player {diags2[0]} is the winner diagonally (\\)!")
		return True

	return False