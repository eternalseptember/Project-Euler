# Problem 6

# The sum of the squares of the first ten natural numbers is
#   1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is
#   3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

sumOfSquare = 0
squareOfSum = 0

for x in range (1,101):
	sumOfSquare += x*x
	squareOfSum += x



print("sum of square: {0}, square of sum: {1}".format(sumOfSquare, squareOfSum))