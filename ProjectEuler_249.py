from sys import argv
from math import sqrt
from pdb import set_trace
import functools

@functools.lru_cache(maxsize=4096)
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
  if n<2: return
  yield 2
  for i in odds(n):
    if i>n: break;
    if isPrime(i): yield i
    
# primeSums[sum] = the number of subsets of the
# nums list that add up to sum
def getPrimeSums(nums):
  primeSums = {}
  primeSums[0] = 1
  for num in nums:
    for sum in list(primeSums)[::-1]:
      if sum+num not in primeSums:
        primeSums[sum+num] = 0
      primeSums[sum+num] += primeSums[sum]
  return primeSums
  
def getCountOfSumsOfPrimeSubsets(upTo):
  primes = getPrimesUpTo(upTo)
  primeSums = getPrimeSums(primes)
  count=0
  for sum in primeSums:
    if isPrime(sum):
      count += primeSums[sum]
  return count

if __name__=="__main__":
  print(getCountOfSumsOfPrimeSubsets(int(argv[1])))