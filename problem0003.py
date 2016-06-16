# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
import math

def findLargestPrime(num):
	number = int(num)
	largestPrime = 1

	upperRange = int(math.sqrt(number)) + 1
	divisor = 2
	while (divisor < upperRange):
		if (number % divisor == 0):
			quotient = number // divisor
			if isPrime(quotient):
				largestPrime = quotient
				break
			else:
				if isPrime(divisor):
					if (divisor > largestPrime):
						largestPrime = divisor
		divisor += 1
	
	# If largestPrime is still one, then number entered is a prime number
	if (largestPrime == 1):
		largestPrime = number

	return largestPrime

def isPrime(num):
	number = int(num)
	""" Checks if an integer is a prime number. """
	if (number <= 1): # 1 isn't a prime number
		return False
	elif (number <= 3): # 2 and 3 are primes
		return True
	elif ((number % 2 == 0) or (number % 3 == 0)):
		return False
	else:
		# Start checking at five.
		# If the number is evenly divisible, then it's not prime.
		# The for loop increments by six because the inner if statement
		#   already checks the next odd number.
		maxDivisor = int(math.sqrt(number))
		for divisor in list(range(5, maxDivisor+1, 6)):
			if ((number % divisor == 0) or (number % (divisor + 2) == 0)):
				return False
		# If the script made it to this point, then it's a prime number.
		return True


number = 600851475143
largestPrime = findLargestPrime(number)
print("Largest Prime: {0}".format(largestPrime))

'''
for i in list(range(2, 21)):
	largestPrime = findLargestPrime(i)
	print("Number: {0}, Largest Prime: {1}".format(i, largestPrime))
'''