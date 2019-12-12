""" A simple codde for minesweeper"""

import random, itertools
import numpy as np

def difficulty():
	diff = input('Input difficulty: ')
	while diff not in ['1','2','3']:
		diff = input("Please input difficulty '1', '2' or '3': ")

def create_grid(size, mines):
	grid = []
	for i in range(size):
		grid.append([0] * size)

	for i in range(mines):

		while True:
			pos = [random.randint(0, size - 1), random.randint(0, size - 1)]
			if grid[pos[0]][pos[1]] != '*':
				grid[pos[0]][pos[1]] = '*'
				break

		for x, y in itertools.product([-1,0,1], repeat = 2):
			if (pos[0] + y) in range(size) and (pos[1] + x) in range(size):
				if grid[pos[0] + y][pos[1] + x] != '*':
					grid[pos[0] + y][pos[1] + x] += 1


	return grid


def display_grid(grid):
	n = len(grid)

	print('╔', end = '')
	for i in range(n - 1):
		print('═══╦', end = '')
	print('═══╗')

	for i in range(n):
		print('║', end = '')
		for j in range(n):
			print(' ' + str(grid[i][j]) + ' ' + '║', end = '')

		if i != n-1:
			print('\n╠', end = '')
			for j in range(n - 1):
				print('═══╬', end = '')
			print('═══╣')
		else:
			print('\n╚', end = '')
			for i in range(n - 1):
				print('═══╩', end = '')
			print('═══╝')


display_grid(create_grid(10, 20))


# def start_game:
# 	diff = difficulty():

# 	if diff == '1':
# 		grid = create_grid(10, 10)
# 	elif diff == '2':
# 		grid = create_grid(20, 20)
# 	else: 
# 		grid == create_grid(50, 100)





