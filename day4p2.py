# bingo
with open('day4.txt') as f:
	lines = f.readlines()

lines = [line.strip('\n') for line in lines]

draw_nums = lines[0].split(',')
boards = []
temp_board = []

for i,line in enumerate(lines[2:]):
	
	if len(line) == 0:
		boards.append(temp_board)
		temp_board = []
	else:
		line = [val for val in line.split(' ') if val != '']
		temp_board.append(line)

boards.append(temp_board)
# create mask filled with zeros to keep track of board filling
board_mask = [[[0 for col in range(len(boards[0][0]))] for row in range(len(boards[0][0]))] for dummy in range(len(boards))]
board_win_mask = [0] * len(boards)

def update_mask(board,num,board_idx):
	for row_idx,row in enumerate(board):
		if num in row:
			board_mask[board_idx][row_idx][row.index(num)] = 1

def they_win(board_num,board_win_mask):
	tally_score(board_num,board_win_mask)

def tally_score(board_num,board_win_mask):
	if sum(board_win_mask) == len(boards):
		score = 0
		for row_num,row in enumerate(boards[board_num]):
			for col,val in enumerate(row):
				if board_mask[board_num][row_num][col] == 0:
					score += int(val)

		print(f"p2: {score*int(num)}")
		exit()

def check_for_win(board_win_mask):
	for i,board in enumerate(board_mask):
		# check rows:
		for row in board:
			if row == [1 for col in range(len(boards[0][0]))]:
				board_win_mask[i] = 1
				they_win(i,board_win_mask)

		# check cols:
		for col in range(len(boards[0][0])):
			col_sum = 0
			for row in board:
				col_sum += row[col]
			if col_sum == len(boards[0][0]):
				board_win_mask[i] = 1
				they_win(i,board_win_mask)

	return board_win_mask

for num_idx,num in enumerate(draw_nums):
	for board_idx,board in enumerate(boards):
		update_mask(board,num,board_idx)
		board_win_mask = check_for_win(board_win_mask)
		


