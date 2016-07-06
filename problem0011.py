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
		grid = file.read().splitlines()
	return grid




grid = turnGridIntoArray("problem0011-grid.txt")
print(grid)