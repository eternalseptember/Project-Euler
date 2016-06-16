# Problem 5

# 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible
# by all numbers from 1 to 20?


def isDivisibleByEachNumber(number):
	""" A function that can check through a list of divisors. """
	for x in range (1, 11):
		if (number % x != 0):
			return False
	return True


initNum = 2520
maxNum = 1

for x in range(11, 21):
	maxNum *= x

print (maxNum)

check = isDivisibleByEachNumber(2520)
print(check)

