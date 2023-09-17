import random
import math
global primes
primes = set()
def init_prime():
	i = 0
	nums = list(range(2,1000001))
	nprimes = set()
	#primes = set()
	while i < len(nums):
		if nums[i] not in nprimes:
			for j in range(nums[i] * nums[i], 1000001, nums[i]):
				nprimes.add(j)
			else:
				primes.add(nums[i])
		i+= 1
def is_prime(n):
	"""
	Returns True if n is prime, otherwise returns False.
	"""
	return n in primes

def sample_in_range(n):
	"""
	Returns a randomly chosen prime in the range 2 throough n.
	This is performed by repeatedly sampling a number in the range 2 through n, and testing if it is prime.
	This function also returns the number of tries taken to find the prime number.
	"""
	count = 0
	while True:
		x = random.randrange(1, n + 1)
		if is_prime(x):
			return (x, count)
		else:
			count += 1
			continue

def expected_tries(n):
	"""
	This function takes the range n as an argument. and performs 10000 trials of sampling a prime number.
	It calls sampleInRange(n) 10000 times, and returns the expected (mean) number of tries taken to find 
	a prime number in the range 2 through n. 
	This function returns one prime number returned through any of the 10000 trials, and the expected number of tries.
	"""
	sum = 0
	p = 0
	for i in range(10000):
		t = sample_in_range(n)
		if i == 0:
			p =t[0]
		sum += t[1]
	return (p ,sum / 10000)

init_prime()
print("n = 1000: " + str(expected_tries(1000)) + " natural log of 1000: " + str(math.log(1000)))
print("n = 10000: " + str(expected_tries(10000)) + " natural log of 10000: " + str(math.log(10000)))
print("n = 100000: " + str(expected_tries(100000)) + " natural log of 100000: " + str(math.log(100000)))
print("n = 1000000: " + str(expected_tries(1000000)) + " natural log of 1000000: " + str(math.log(1000000)))

