import math

def factorize(n):
  if is_prime(n):
    factors.append(n)
  else:
    for i in range(2,n):
      if (n%i) == 0:
        factors.append(i)
        factorize(int(n/i))
        break

def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True



n = int(input("Enter a number: "))
global factors
factors = list()
factorize(n)
print("The set of prime factors are:")
for i in factors:
  print(i)

