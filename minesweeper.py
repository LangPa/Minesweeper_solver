""" A simple codde for minesweeper"""

import random, itertools, sys
import numpy as np
from time import time
from scipy import optimize

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
		game_finished_ (bool): game finished or not
		height_ (int): height of minefield
		width_ (int): width of minefield
		mines_ (int): number of mines remaining
		remain_ (int): number of squares to clear
		false_positives_ (int): number of squares incorrectly flagged
		true_positives_ (int): number of correctly flagged squares
	"""
	def __init__(self, start = (5,5), difficulty = 3):
		self.start = start
		self.difficulty = difficulty
		self.false_positives_ = 0
		self.true_positives_ = 0
		self.game_finished_ = True

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
			pos.pop(pos_x)

		field = []
		for i in range(height):
			field.append([' '] * width)

		self.minefield_ = field
		self.solution_ = grid
		self.height_ = height
		self.width_ = width
		self.mines_ = mines
		self.remain_ = height * width - mines
		self.game_finished_ = False
		self.unveil(self.start)
		self.start_time_ = time()

		return self

	def timer(self):
		print(f'{time() - self.start_time_}s')
		self.time_ = time() - self.start_time_

	def flag(self, choice):
		"""
		Flags square for mine

		Args:
			choice (tuple): chosen square

		Returns:
			self: updated minefield
		"""
		if self.game_finished_:
			print('Game is finished, reset to start again.')
			return self

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

		height = self.height_
		width = self.width_

		print('     ', end = '')
		for i in range(width):
			if i > 9:
				print(i, end = '  ')
			else:
				print(i, end = '   ')
		print('')

		print('   ╔', end = '')
		for i in range(width - 1):
			print('═══╦', end = '')
		print('═══╗')

		for i in range(height):
			if i < 10:
				print(i, end = '  ║')
			else:
				print(i, end = ' ║')
			for j in range(width):
				print(' ' + str(grid[i][j]) + ' ' + '║', end = '')

			if i != height - 1:
				print('\n   ╠', end = '')
				for j in range(width - 1):
					print('═══╬', end = '')
				print('═══╣')
			else:
				print('\n   ╚', end = '')
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
		if self.game_finished_:
			print('Game is finished, reset to start again.')
			return self

		height = len(self.minefield_)
		width = len(self.minefield_[0])

		if self.solution_[choice[0]][choice[1]] == '*':
			self.reveal(choice)
		
		elif self.minefield_[choice[0]][choice[1]] != ' ':
			pass

		elif self.solution_[choice[0]][choice[1]] == 0:
			self.solution_[choice[0]][choice[1]] = 9
			self.minefield_[choice[0]][choice[1]] = 0
			self.remain_ -= 1
			for x, y in itertools.product([-1,0,1], repeat = 2):
				if (choice[0] + y) in range(height) and (choice[1] + x) in range(width):
					if self.minefield_[choice[0] + y][choice[1] + x] != ' ':
						continue
					self.unveil((choice[0] + y, choice[1] + x))
			self.solution_[choice[0]][choice[1]] = 0

		else:
			self.minefield_[choice[0]][choice[1]] = self.solution_[choice[0]][choice[1]]
			self.remain_ -= 1
		
		if self.remain_ == 0:
			print('Complete!')
			self.reveal()
		
		return self

	def reveal(self, choice = None):
		"""
		Reveals the position of all the mines and ends the game
		"""

		for i in range(self.height_):
			for j in range(self.width_):
				if (i,j) == choice:
					self.minefield_[i][j] = '!'
				elif self.minefield_[i][j] == 'F':
					if self.solution_[i][j] != '*':
						self.minefield_[i][j] = 'X'
				elif self.solution_[i][j] == '*':
					self.minefield_[i][j] = '*'
		self.display()
		self.game_finished_ = True
		self.timer()
		return self
		
	def OLSsolve(self, precision = 0.001):
		"""
		Method employing the Ordinary Least Squares estimation to uncover squares

		Returns:
			self: minefield with all certain mines flagged and certain clear squares uncovered
		"""

		if self.game_finished_:
			print('Game is finished, reset to start again.')
			return self

		# Create matrix of linear equations of covered squares
		# Squares are considered only if they are adjactent to an uncovered square and is not flagged
		squares = {}
		nbhr = []
		for i in range(self.height_):
			for j in range(self.width_):
				a = self.minefield_[i][j]
				flags = 0
				if a in range(1,9):
					for x, y in itertools.product([-1,0,1], repeat = 2):
						if (i + y) in range(self.height_) and (j + x) in range(self.width_):
							if self.minefield_[i + y][j + x] == ' ':
								squares[(i,j)] = squares.get((i,j), []) + [(i + y, j + x)]
								if (i + y,j + x) not in nbhr:
									nbhr += [(i + y,j + x)]
							elif self.minefield_[i + y][x + j] == 'F':
								flags += 1
					if (i,j) in squares.keys():
						squares[(i,j)] += [a - flags]
		
		X = np.zeros((len(squares), len(nbhr)))
		y = np.asarray([value[-1] for key, value in squares.items()])
		for index, items in enumerate(squares.items()):
			for adj in items[1][:-1]:
				X[index, nbhr.index(adj)] = 1
		

		# beta = np.linalg.lstsq(X,y, rcond=-1)
		# beta = optimize.nnls(X, y)
		beta = optimize.lsq_linear(X, y, (0,1))
		b_true = []
		for pos in nbhr:
			b_true += [self.solution_[pos[0]][pos[1]]]		
		
		change = False
		selection = []
		while not change:
			print(f'precision: {precision}')
			for a,b,c in zip(beta['x'], b_true, nbhr):
				print(f'predict: {a:.3f}, true: {b}, {c}')
				if self.game_finished_:
					break
				if a < precision and a > 0 - precision:
					# print(f'predict: {a:.3f}, true: {b}, {c}')
					if b == '*':
						print('false negative')
					self.unveil(c)
					change = True
				elif a > 1 - precision and a < 1 + precision:
					selection += [c]
					# print(f'predict: {a:.3f}, true: {b}, {c}')
					if b != '*':
						print('false positive')
					self.flag(c)
					change = True
				
			precision += 0.005

		

Game = game(difficulty = 3)	
Game.create_grid()

# Game.display()
# Game.OLSsolve()
# Game.display()
# Game.OLSsolve()
# Game.display()
# Game.OLSsolve()
# print(Game.time_)
# Game.display()

while not Game.game_finished_:
	Game.display()
	print(Game.remain_)
	Game.OLSsolve()