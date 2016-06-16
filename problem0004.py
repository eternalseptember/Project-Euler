# Problem 4

# A palindromic number reads the same both ways. The largest 
# palindrome made from the product of two 2-digit numbers is
# 9009 = 91*99.

# Find the largest palindrome made from the product of two
# 3-digit numbers

def isPalindrome(num):
	""" Checks if the number is a palindrome """
	if (str(num) == str(num)[::-1]):
		return True
	else:
		return False

largestPalindrome = 0

for x in range (1, 1000):
	for y in range (1, 1000):
		product = x * y
		if isPalindrome(product):
			if (product > largestPalindrome):
				largestPalindrome = product

print (largestPalindrome)

'''
print("Is 909 a palindrome? {0}".format(isPalindrome(909)))
print("Is 900 a palindrome? {0}".format(isPalindrome(900)))
'''