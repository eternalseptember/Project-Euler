# Problem 9

# A Pythagorean triplet is a set of three natural numbers,
#   a < b < c, for which a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which
# a + b + c = 1000.
# Find the product a*b*c.


def findPythagoreanTriple(totalSum):
	""" 
	Takes the sum of a + b + c as parameter. 
	Implements Euclid's formula.
	"""
	upperRange = totalSum // 2

	for m in range(2, upperRange):
		# If m > n, then n's max is m - 1
		# But range doesn't include the last number.
		for n in range(1, m):
			# initial values for (3,4,5) triplet:
			# m = 2, n = 1
			a = m*m - n*n 
			b = 2*m*n 
			c = m*m + n*n

			if (a+b+c == totalSum):
				product = a*b*c
				return [[a, b, c], product]




[triplet, product] = findPythagoreanTriple(1000)
print("Triplet: {0}. Product: {1}".format(triplet, product))