from sys import argv
from math import sqrt
from pdb import set_trace
import functools

@functools.lru_cache(maxsize=65536)
def isPrime(n):
  for i in getPrimesUpTo(int(sqrt(n))):
    if n%i==0: return False
  return True

def odds(endingAt, startingAt=3):
  i=startingAt
  while i<=endingAt:
    yield i
    i+=2
  
def getPrimesUpTo(n):
  yield 2
  if n<=2: return
  for i in odds(n):
    if isPrime(i): yield i
    if i+2>n: break;

def getPrimeSubsetSumsUpTo(n):
  for u in getPrimeUpTo(n):
    sum = u
    if isPrime(sum): yield sum

if __name__=="__main__":
  ps = list(getPrimesUpTo(int(argv[1])))
  print(ps)
  print(len(ps))