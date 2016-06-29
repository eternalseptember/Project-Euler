# Problem 7

# By listing the first six prime numbers: 
#   2, 3, 5, 7, 11, and 13
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from math import log

def sieve_erasthanos(n):
	""" Find the nth prime number. """

	# create large array and initialize to true
	maxLength = int(2 * n * log(n))
	sieve = [True] * maxLength
	primeNum = 0

	for i in range(2, maxLength):
		if sieve[i]:	# Starts with 2, which is a prime
			primeNum += 1
			if primeNum == n:
				return i
			for j in range(2*i, maxLength, i):	# cross off all multiples of i
				sieve[j] = False



ans = sieve_erasthanos(10001)
print("The 10001st prime number is {0}.".format(ans))