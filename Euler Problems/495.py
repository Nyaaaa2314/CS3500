#block comment
"""
<p>Let $W(n,k)$ be the number of ways in which $n$ can be written as the product of $k$ distinct positive integers.</p>
<p>For example, $W(144,4) = 7$. There are $7$ ways in which $144$ can be written as a product of $4$ distinct positive integers:</p>
<p></p><ul><li>$144 = 1 \times 2 \times 4 \times 18$</li>
<li>$144 = 1 \times 2 \times 8 \times 9$</li>
<li>$144 = 1 \times 2 \times 3 \times 24$</li>
<li>$144 = 1 \times 2 \times 6 \times 12$</li>
<li>$144 = 1 \times 3 \times 4 \times 12$</li>
<li>$144 = 1 \times 3 \times 6 \times 8$</li>
<li>$144 = 2 \times 3 \times 4 \times 6$</li>
</ul><p>Note that combinations of the integers themselves are not considered distinct.</p>
<p>Furthermore, $W(100!,10)$ modulo $1\,000\,000\,007 = 287549200$.</p>
<p>Find $W(10000!,30)$ modulo $1\,000\,000\,007$.</p>
"""
import sys
import itertools

global maxfactor
global primes
global n
global k
global total
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def initPrimes():
    nums = open("primes-million.txt").read().split()
    for i in nums:
        primes.add(int(i))
def processInput(s):
    try:
        return int(s)
    except:
        try:
            return factorial(int(s.split("!")[0]))
        except:
            return ValueError
        
def makeLists(lst, rt, size):
    if size == k:
        if rt == n:
            total += 1
        return
    else:
        for i in range(maxfactor + 1):
            if(i * rt > n):
                return
            else:
                lst.append(i)
                makeLists(lst, rt * i, size + 1)
                lst.pop()


sys.set_int_max_str_digits(100000)

#Initializing variables
primes = set()
initPrimes()
n = processInput(input("Enter n: "))
k = int(input("Enter k: "))
maxfactor = int(n / factorial(k - 1))
MOD = 1000000007

#Base cases
if factorial(k) > n:
    print(0)
    exit()
if factorial(k) == n:
    print(1)
    exit() 
nums = list(range(1, maxfactor + 1))

valid = 0
#combinations = list(itertools.combinations(nums, k))
#print(combinations)
repeats = set()
for i in combinations:
    total = 1
    for j in i:
        total *= j
        if total > n:
            break
    if total == n:
        valid += 1
    # if total > n:
    #     break
print(valid)


