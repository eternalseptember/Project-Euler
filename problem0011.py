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
	greatestProduct = 0

	# range excludes last number
	for y in range(0, listSize): # row
		
		for x in range(0, listSize): # column
			# if (x+1) < listSize
			#   then don't search left
			# if (x+adjacentNum >= listSize)
			# then don't search right.




grid = turnGridIntoArray("problem0011-grid.txt")
searchAdjacentNumbersInGrid(grid, 4)