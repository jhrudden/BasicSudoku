import numpy as np



class SudokuSolver:
	def __init__(self, board):
		self.board = board

	def get_row(self, r_index):
		# find each number in a given row index
		return self.board[r_index]

	def get_col(self, col_index):
		# find all numbers in a col at a given index
		col = []
		for row in range(9):
			col.append(self.board[row][col_index])

		return col


	def get_box(self, r_index, col_index):
		# find the 3 x 3 box this coord pair is in
		box = []
		# check if the number already exists inside its square
		row_0 = (r_index // 3)*3
		col_0 = (col_index // 3)*3

		# iterate throw each cell in this box
		for k in range(3):
			for l in range(3):
				# add each number in this box to an array
				sqr_r_index = row_0+k
				sqr_c_index = col_0+l
				item = self.board[sqr_r_index][sqr_c_index ]
				box.append(item)

		return box

	def all_possibilities(self, r_index, col_index):
		# create a set of all possible values for an arbitrary cell
		poss = set(range(1,10))
		# grab the row + col + box for the given coords
		row = self.get_row(r_index)
		col = self.get_col(col_index)
		box = self.get_box(r_index, col_index)

		for item in row + col + box:
			# if values from our row col or box are in the poss set
			# remove them
			if item in poss:
				poss.remove(item)
		return poss


	def solve(self):
		unsolved = True
		# continue to solve this board if it is unsolved
		while unsolved:
			unsolved = False

			# iterate down the cells of the board
			for row in range(9):
				for col in range(9):

					# if a current cell is empty, then try to fill it
					if (self.board[row][col] == 0):
						unsolved = True

						# grab all possible numbers that can be placed in
						# this cell
						poss = self.all_possibilities(row, col)

						# if there is only 1 number to fill this slot, then
						# fill it
						if (len(poss) == 1):
							self.board[row][col] = list(poss)[0]










board = [[4,7,0,0,0,0,0,0,0],
[0,6,2,5,9,0,0,3,0],
[0,3,8,7,0,4,2,0,9],
[8,0,1,2,5,0,4,0,3],
[0,4,0,0,7,1,0,0,6],
[7,2,0,3,0,0,8,0,0],
[0,0,0,0,0,0,0,0,0],
[9,0,0,4,0,7,5,0,8],
[2,0,0,0,8,0,0,9,7]]
grid = SudokuBoard(board)


grid.solve()
print(np.array(grid.board))
