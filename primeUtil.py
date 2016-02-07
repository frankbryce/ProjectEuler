from math import sqrt
import functools

@functools.lru_cache(maxsize=4096)
def isPrime(n):
  if n<2: return False
  for i in getPrimesUpTo(int(sqrt(n))):
    if n%i==0: return False
  return True

def odds(endingAt, startingAt=3):
  i=startingAt
  while i<=endingAt:
    yield i
    i+=2
  
def getPrimesUpTo(n, startingAt=2):
  if n<startingAt: return
  if startingAt==2: yield 2
  for i in odds(n, max(3,startingAt)):
    if i>n: break;
    if isPrime(i): yield i
    