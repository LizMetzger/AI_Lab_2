QUEENS = 10

# function to count the number of attacks on the board
def attacks(queens):
	attacks = 0
	# look at each queen
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
					attacks += 1
			y_itter += 1
			x_itter += 1
		# count attacks horizontally up (to the right)
		y_itter = current_queen[0] - 1
		x_itter = current_queen[1] + 1
		while x_itter < 10 and y_itter >= 0:
			for k in range(current_queen[1], QUEENS):
				if queens[k] == [y_itter, x_itter]:
					attacks += 1
			y_itter -= 1
			x_itter += 1
	return attacks

# move the queens to each possible spot and find the move with the lowest attacks
def move(queens, total_attacks):
	lowest_attacks = total_attacks
	lowest_ind = [-1, -1]
	# for each queen
	for i in range(QUEENS):
		# save its original position
		set = []
		for val in queens[i]:
			set.append(val)
		# move it down its column looking for less attacks
		for j in range(QUEENS):
			queens[i][0] = j
			new_attacks = attacks(queens)
			# if there are less attacks save that number and the move
			if new_attacks < lowest_attacks:
				lowest_attacks = new_attacks
				lowest_ind[0] = i
				lowest_ind[1] = j
		# reset the queens position before looking at another one
		queens[i] = set
	return lowest_ind, lowest_attacks

def gradient_search(board):
	# array of my queen's locations
	queens = []
	# variable for if its been solved yet
	solved = False
	# find my queens in the board (so x is ascending)
	for x in range(QUEENS):
		for y in range(QUEENS):
			if board[y][x] == 1:
				queens.append([y,x])
				board[y][x] = 0
	# find the number of attacks
	num_attacks = attacks(queens)
	minimizing = True
	# find the best move to make, keep making moves until there are no better ones
	while minimizing == True:
		best_move, num_attacks = move(queens, num_attacks)
		# if the array is NOT [-1, -1] then there is a best move, make it
		if best_move[0] >= 0:
			# pick the right queen (best_move[0]) and set its y value to be correct (best_move[1])
			queens[best_move[0]][0] = best_move[1]
		# else leave loop and check if its solved
		else:
			minimizing = False
	# set the map to have the position of the queens
	for queen in queens:
		board[queen[0]][queen[1]] = 1
	# if attacks is 0 then return True 
	if attacks(queens) == 0:
		solved = True
	return solved