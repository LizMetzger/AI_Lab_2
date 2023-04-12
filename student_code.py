QUEENS = 10

def attacks(queens):
	attacks = 0
	for i in range(QUEENS):
		current_queen = queens[i]
		# count attacks in the row (to the right)
		for j in range(current_queen[1] + 1, QUEENS):
			check_queen = queens[j]
			if check_queen[0] == current_queen[0]:
				attacks += 1
		# count attacks horzintally down (to the right)
		y_itter = current_queen[0] + 1
		x_itter = current_queen[1] + 1
		while x_itter < 10 and y_itter < 10:
			for k in range(current_queen[1], QUEENS):
				if queens[k] == [y_itter, x_itter]:
					print("DOWN: check", queens[k], "current", [y_itter, x_itter])
					attacks += 1
			y_itter += 1
			x_itter += 1
		# count attacks horizontally up (to the right)
		y_itter = current_queen[0] - 1
		x_itter = current_queen[1] + 1
		while x_itter < 10 and y_itter >= 0:
			for k in range(current_queen[1], QUEENS):
				if queens[k] == [y_itter, x_itter]:
					print("UP: check", queens[k], "current", [y_itter, x_itter], "queen", current_queen)
					attacks += 1
			y_itter -= 1
			x_itter += 1
	return attacks

def gradient_search(board):
	queens = []
	# find my queens in the board (so x is ascending)
	for x in range(QUEENS):
		for y in range(QUEENS):
			if board[y][x] == 1:
				queens.append([y,x])
	# print('queens: ', queens)
	# find the number of attacks
	num_attacks = attacks(queens)
	print("num_attacks:", num_attacks)
	# if attacks is 0 then return True 
	# else return False

