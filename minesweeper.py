""" A simple codde for minesweeper"""

import random, itertools, sys
import numpy as np

class game:
	"""
	Minesweeper game
	Must run create_grid method to initialise game

	Args:
		difficulty (int): Difficulty in range 1 (easy) to 3 (hard)
		start (tuple): Starting square

	Attributes:
		minefield_ (list): Current minefield
		solution_ (list): Full solution
	"""
	def __init__(self, start = (5,5), difficulty = 3):
		self.start = start
		self.difficulty = difficulty
		self.false_positives_ = 0
		self.true_positives_ = 0

	def reset(self, start = None, difficulty = None):
		"""
		Resets the game

		Args:
			difficulty (int): Difficulty in range 1 (easy) to 3 (hard)
			start (tuple): Starting square

		Returns:
			self: Reset game
		"""
		if start:
			self.start = start
		if difficulty:
			self.difficulty = difficulty

		self.create_grid()

		return self

	def create_grid(self):
		"""
		Creates minefield

		Returns:
			self: Minefield grid and solution
		"""
		
		if self.difficulty == 1:
			height, width, mines = (9, 9, 10)

		elif self.difficulty == 2:
			height, width, mines = (16, 16, 40)

		else: 
			height, width, mines = (16, 30, 99)

		grid = []
		pos = [x for x in itertools.product(range(height), range(width))]

		for i in range(height):
			grid.append([0] * width)

		for x, y in itertools.product([-1,0,1], repeat = 2):
			if (self.start[0] + y) in range(height) and (self.start[1] + x) in range(width):
				pos.remove((self.start[0] + y, self.start[1] + x))

		for i in range(mines):

			pos_x = random.randint(0,len(pos) - 1)
			grid[pos[pos_x][0]][pos[pos_x][1]] = '*'

			for x, y in itertools.product([-1,0,1], repeat = 2):
				if (pos[pos_x][0] + y) in range(height) and (pos[pos_x][1] + x) in range(width):
					if grid[pos[pos_x][0] + y][pos[pos_x][1] + x] != '*':
						grid[pos[pos_x][0] + y][pos[pos_x][1] + x] += 1
		
		field = []
		for i in range(height):
			field.append([' '] * width)

		self.minefield_ = field
		self.solution_ = grid
		self.mines_ = mines
		self.unveil(self.start)

		return self

	def flag(self, choice):
		"""
		Flags square for mine

		Args:
			choice (tuple): chosen square

		Returns:
			self: updated minefield
		"""

		if self.minefield_[choice[0]][choice[1]] == ' ':

			self.minefield_[choice[0]][choice[1]] = 'F'
			self.mines_ -= 1

			if self.solution_[choice[0]][choice[1]] == '*':
				self.true_positives_ += 1
			else: 
				self.false_positives_ += 1

		return self

	def display(self, grid = None):
		"""
		displays grid on terminal

		"""
		if not grid:
			grid = self.minefield_

		height = len(grid)
		width = len(grid[0])
		print('╔', end = '')
		for i in range(width - 1):
			print('═══╦', end = '')
		print('═══╗')

		for i in range(height):
			print('║', end = '')
			for j in range(width):
				print(' ' + str(grid[i][j]) + ' ' + '║', end = '')

			if i != height - 1:
				print('\n╠', end = '')
				for j in range(width - 1):
					print('═══╬', end = '')
				print('═══╣')
			else:
				print('\n╚', end = '')
				for i in range(width - 1):
					print('═══╩', end = '')
				print('═══╝')

	def unveil(self, choice):
		"""
		Unveils square

		Args:
			choice (tuple): square chosen

		Returns:
			self: unpdated grid
		"""
		height = len(self.minefield_)
		width = len(self.minefield_[0])

		if self.solution_[choice[0]][choice[1]] == '*':
			print('boom')
			for i in range(height):
				for j in range(width):
					if self.solution_[i][j] == '*':
						self.minefield_[i][j] = '*'
			self.display()
			self.reset
			return 'Boom'

		elif self.solution_[choice[0]][choice[1]] == 0:
			self.solution_[choice[0]][choice[1]] = 9
			for x, y in itertools.product([-1,0,1], repeat = 2):
				if (choice[0] + y) in range(height) and (choice[1] + x) in range(width):
					if self.minefield_[choice[0] + y][choice[1] + x] != ' ':
						continue
					self.unveil((choice[0] + y, choice[1] + x))
			self.solution_[choice[0]][choice[1]] = 0
			self.minefield_[choice[0]][choice[1]] = self.solution_[choice[0]][choice[1]]
			return self

		else:
			self.minefield_[choice[0]][choice[1]] = self.solution_[choice[0]][choice[1]]
			return self

# def start_game(self):

# 	answ = create_grid()
# 	grid = []
# 	for i in range(height):
# 		grid.append([' '] * width)

# 	grid = unveil(grid, answ, self.start)
# 	display_grid(grid)

# 	to_clear = height * width - mines

# 	while grid != 'Boom':
# 		print('Input choice')
# 		while True:
# 			try:
# 				choice = int(input('row: ')), int(input('column: '))
# 				break
# 			except:
# 				if input('please enter a number in the correct range, or press q to quit: ') == 'q':
# 					sys.exit()


# 		grid = unveil(grid, answ, choice)
# 		display_grid(grid)

# 		cleared = 0
# 		for row in grid:
# 			for square in row:
# 				if square != ' ':
# 					cleared += 1
# 		if cleared == to_clear:
# 			print('Congratulations!')
# 			break

