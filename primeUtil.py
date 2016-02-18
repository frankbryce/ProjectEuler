from math import sqrt
import functools

# returns whether n is a prime number
@functools.lru_cache(maxsize=4096)
def isPrime(n):
  if n<2: return False
  for i in getPrimesUpTo(int(sqrt(n))):
    if n%i==0: return False
  return True

# iterates through odd numbers starting at startingAt
def odds(endingAt, startingAt=3):
  i=startingAt
  while i<=endingAt:
    yield i
    i+=2

# generator for primes up to n, starting at startingAt
def getPrimesUpTo(n, startingAt=2):
  if n<startingAt: return
  if startingAt==2: yield 2
  for i in odds(n, max(3,startingAt)):
    if i>n: break;
    if isPrime(i): yield i

# gets cardinality of the prime factors of n
@functools.lru_cache(maxsize=256)
def factorCardByPrime(n):
    if n==0 or n==1: return {}
    for prime in getPrimesUpTo(sqrt(n)):
        if n%prime==0:
            card=factorCardByPrime(n/prime).copy()
            if prime not in card:
                card[prime]=1
            else:
                card[prime]+=1
            return card
    return {int(n): 1}

# gets the cardinality of the prime factors of n!
@functools.lru_cache(maxsize=256)
def factorCardByPrimeFactorial(n):
    card={}
    for i in range(2,n+1):
        c = factorCardByPrime(i)
        for prime in c:
            if prime not in card:
                card[prime]=0
            card[prime]+=c[prime]
    return card
