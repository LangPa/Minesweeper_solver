""" A simple codde for minesweeper"""

import random, itertools, sys
import numpy as np

# def difficulty():
# 	diff = input('Input difficulty: ')
# 	while diff not in ['1','2','3']:
# 		diff = input("Please input difficulty '1', '2' or '3': ")

def create_grid(height, width, mines, initial):
	grid = []
	pos = [x for x in itertools.product(range(height), range(width))]

	for i in range(height):
		grid.append([0] * width)

	for x, y in itertools.product([-1,0,1], repeat = 2):
		if (initial[0] + y) in range(height) and (initial[1] + x) in range(width):
			pos.remove((initial[0] + y, initial[1] + x))

	for i in range(mines):

		pos_x = random.randint(0,len(pos) - 1)
		print(pos[pos_x][0], pos[pos_x][1])
		grid[pos[pos_x][0]][pos[pos_x][1]] = '*'

		for x, y in itertools.product([-1,0,1], repeat = 2):
			if (pos[pos_x][0] + y) in range(height) and (pos[pos_x][1] + x) in range(width):
				if grid[pos[pos_x][0] + y][pos[pos_x][1] + x] != '*':
					grid[pos[pos_x][0] + y][pos[pos_x][1] + x] += 1

	print(grid)
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


# display_grid(create_grid(16, 30, 99, (10,1)))

def start_game(initial, diff = 3):
	if diff == 1:
		height, width, mines = (9, 9, 10)

	elif diff == 2:
		height, width, mines = (16, 16, 40)

	else: 
		height, width, mines = (16, 30, 99)

	answ = create_grid(height, width, mines, initial)
	grid = []
	for i in range(height):
		grid.append([' '] * width)

	grid = unveil(grid, answ, initial)
	display_grid(grid)

	to_clear = height * width - mines

	while grid != 'Boom':
		print('Input choice')
		while True:
			try:
				choice = int(input('row: ')), int(input('column: '))
				break
			except:
				if input('please enter a number in the correct range, or press q to quit: ') == 'q':
					sys.exit()


		grid = unveil(grid, answ, choice)
		display_grid(grid)

		cleared = 0
		for row in grid:
			for square in row:
				if square != ' ':
					cleared += 1
		if cleared == to_clear:
			print('Congratulations!')
			break

		



def unveil(grid, answ, choice):
	height = len(grid)
	width = len(grid[0])

	if answ[choice[0]][choice[1]] == '*':
		print('boom')
		return 'Boom'

	elif answ[choice[0]][choice[1]] == 0:
		answ[choice[0]][choice[1]] = 9
		for x, y in itertools.product([-1,0,1], repeat = 2):
			if (choice[0] + y) in range(height) and (choice[1] + x) in range(width):
				if grid[choice[0] + y][choice[1] + x] != ' ':
					continue
				grid = unveil(grid, answ, (choice[0] + y, choice[1] + x))
		answ[choice[0]][choice[1]] = 0
		grid[choice[0]][choice[1]] = answ[choice[0]][choice[1]]
		return grid


	else:
		grid[choice[0]][choice[1]] = answ[choice[0]][choice[1]]
		return grid

			

start_game((5,5), 3)