""" A simple codde for minesweeper"""

import random, itertools
import numpy as np

def difficulty():
	diff = input('Input difficulty: ')
	while diff not in ['1','2','3']:
		diff = input("Please input difficulty '1', '2' or '3': ")

def create_grid(height, width, mines):
	grid = []
	for i in range(height):
		grid.append([0] * width)

	for i in range(mines):

		while True:
			pos = [random.randint(0, height - 1), random.randint(0, width - 1)]
			if grid[pos[0]][pos[1]] != '*':
				grid[pos[0]][pos[1]] = '*'
				break

		for x, y in itertools.product([-1,0,1], repeat = 2):
			if (pos[0] + y) in range(height) and (pos[1] + x) in range(width):
				if grid[pos[0] + y][pos[1] + x] != '*':
					grid[pos[0] + y][pos[1] + x] += 1


	return grid


def display_grid(grid):
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


display_grid(create_grid(16, 30, 99))


def start_game:
	diff = difficulty():
	if diff == '1':
		height, width, mines = (9, 9, 10)

	elif diff == '2':
		height, width, mines = (16, 16, 40)

	else: 
		height, width, mines = (9, 9, 10)

	answ = create_grid(height, width, mines)
	grid = []
	for i in range(height):
		grid.append([0] * width)






