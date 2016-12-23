# Problem 11

# In a 20x20 grid, four numbers along a diagonal line was marked.
# The product of these numbers is 26*63*78*14 = 1788696.

# What is the greatest product of four adjacent numbers in the
# same direction (up, down, left, right, or diagonally) in the
# 20x20 grid?


def turnGridIntoArray(filename):
	"""
	Copied the grid and pasted it into a text file.
	Supply this text file, and it will turn it into an
	  index-able grid.
	"""
	with open(filename) as file:
		grid = []
		for line in file:
			grid.append(line.split())
	return grid


def searchAdjacentNumbersInGrid(grid, adjacentNum):
	listSize = len(grid)
	rangeLimit = listSize - adjacentNum + 1  # range excludes last number
	greatestProduct = 0

	# grid[0][0] = 08
	# grid[1][0] = 49
	# grid[0][1] = 02

	# search vertically
	# 51267216
	for column in range(0, listSize):
		for row in range(0, rangeLimit):
			product = 1
			for i in range(0, adjacentNum):
				product *= int(grid[row + i][column])
			if product > greatestProduct:
				greatestProduct = product

	# search horizonally
	# 48477312
	for row in range(0, listSize):
		for column in range(0, rangeLimit):
			product = 1
			for i in range(0, adjacentNum):
				product *= int(grid[row][column + i])
			if product > greatestProduct:
				greatestProduct = product

	# search left-to-right diagonal


	# search right-to-left diagonal

	return greatestProduct




grid = turnGridIntoArray("problem0011-grid.txt")
greatestProduct = searchAdjacentNumbersInGrid(grid, 4)
print(greatestProduct)


