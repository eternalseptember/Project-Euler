# Problem 5

# 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible
# by all numbers from 1 to 20?


def isDivisibleByEachNumber(number):
	""" A function that can check through a list of divisors. """
	for x in range (11, 21):
		if (number % x != 0):
			print("Failed at {0}".format(x))
			return False
	return True



"""
11
12 -> divisible by 2, 3, 4, 6
13
14 -> divisible by 2, 7
15 -> divisible by 3, 5
16 -> divisible by 2, 4, 8
17
18 -> divisible by 2, 3, 6, 9
19
20 -> divisible by 2, 4, 5, 10
"""


# Is evenly divisible by 1-10, so use this as a base.
initNum = 2520 

# Based on the math in the comments, tried multiplying by the primes.
product = initNum * 11 * 13 * 17 * 19
result = isDivisibleByEachNumber(product)
print("product: {0}, result: {1}".format(product, result))
# isDivisibleByEachNumber failed at multiplying by 16.


# Then product was multipled by 16, and isDivisibleByEachNumber passed.
product = initNum * 11 * 13 * 17 * 19 * 16
result = isDivisibleByEachNumber(product)
print("product: {0}, result: {1}".format(product, result))

# Then product was multipled by 8, and isDivisibleByEachNumber passed.
product = initNum * 11 * 13 * 17 * 19 * 8
result = isDivisibleByEachNumber(product)
print("product: {0}, result: {1}".format(product, result))

# Then product was multipled by 4, and isDivisibleByEachNumber passed.
product = initNum * 11 * 13 * 17 * 19 * 4
result = isDivisibleByEachNumber(product)
print("product: {0}, result: {1}".format(product, result))

# Then product was multipled by 2, and isDivisibleByEachNumber passed.
product = initNum * 11 * 13 * 17 * 19 * 2
result = isDivisibleByEachNumber(product)
print("product: {0}, result: {1}".format(product, result))
# And this is the smallest number that is evenly divisible by 1-20