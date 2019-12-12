""" A simple codde for minesweeper"""

import random, itertools
import numpy as np


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

# print(create_grid(10, 5))

for row in create_grid(20, 20):
	print(row)


