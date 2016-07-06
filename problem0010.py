# Problem 10

# The sum of the primes below 10 is
#   2+3+5+7 = 17

# Find the sum of all the primes below two million.

def sumOfPrimesBelow(n):
	""" Modifying the Sieve of Erasthanos to generate sum. """

	# create large array and initialize to true
	maxLength = n
	sieve = [True] * maxLength
	primeSum = 0

	for i in range(2, maxLength):
		if sieve[i]:	# Starts with 2, which is a prime
			primeSum += i
			for j in range(2*i, maxLength, i):	# cross off all multiples of i
				sieve[j] = False

	return primeSum

sum = sumOfPrimesBelow(2000000)
print("Sum: {0}".format(sum))