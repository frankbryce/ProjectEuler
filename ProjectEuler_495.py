from math import sqrt,factorial
from primeUtil import getPrimesUpTo
from iterUtil import dictIter
from sys import argv
import functools
import pdb

# partitionsOf[i] = number of partitions of i
# only first 30 are here since that's all that
# 495 will require (if even that)
partitionsOf = [1, 1, 2, 3, 5, 
                7, 11, 15, 22, 30, 
                42, 56, 77, 101, 135, 
                176, 231, 297, 385, 490, 
                627, 792, 1002, 1255, 1575, 
                1958, 2436, 3010, 3718, 4565, 
                5604]
  
@functools.lru_cache(maxsize=4096)
def factorCardByPrime(n):
  if n==0 or n==1: return 0
  for prime in getPrimesUpTo(sqrt(n)):
    if n%prime==0:
      card=factorCardByPrime(n/prime)
      if prime not in card:
        card[prime]=1
      else:
        card[prime]+=1
      return card
  return {int(n): 1}

@functools.lru_cache(maxsize=4096)
def factorCardByPrimeFactorial(n):
  card={}
  for i in range(2,n+1):
    c = factorCardByPrime(i)
    for prime in c:
      if prime not in card:
        card[prime]=0
      card[prime]+=c[prime]
  return card

@functools.lru_cache(maxsize=4096)
def nCr(n,r):
  if n<r: return 0
  return int(factorial(n)/factorial(n-r)/factorial(r))

def W2(n,m):
  cardByPrime = factorCardByPrime(n)
  cnt = 1
  for prime in cardByPrime:
    cnt *= nCr(cardByPrime[prime]+m-1,m-1)
  cnt2 = 1
  for prime in cardByPrime:
    cnt2 *= nCr(cardByPrime[prime]+m-3,m-3)
  return cnt,cnt2

def W(n,m):
  cardByPrime = factorCardByPrimeFactorial(n)
  cnt = 1
  for prime in cardByPrime:
    cnt *= nCr(cardByPrime[prime]+m-1,m-1)
  cnt2 = 1
  for prime in cardByPrime:
    cnt2 *= nCr(cardByPrime[prime]+m-3,m-3)
  return cnt/cnt2
  
def getPrimeTuples(cardByPrime, ofLength):
  def getFactorCountTuples(cardByPrime, dictsSoFar):
    nonlocal ofLength
    if len(dictsSoFar)==ofLength:
      for prime in cardByPrime:
        if cardByPrime[prime]!=0:
          return
      yield set(map(lambda d: tuple(d.values()),dictsSoFar))
    else:
      for d in dictIter(cardByPrime):
        if d not in dictsSoFar:
          newCardByPrime = cardByPrime.copy()
          newDictsSoFar = dictsSoFar.copy()
          newDictsSoFar.append(d.copy())
          for prime in d:
            newCardByPrime[prime] -= d[prime]
          for tup in getFactorCountTuples(newCardByPrime, newDictsSoFar):
            yield tup
          
  tups = []
  for tup in getFactorCountTuples(cardByPrime, []):
    if tup not in tups:
      tups.append(tup)
  return tups

if __name__=="__main__":
  # print(factorCardByPrimeFactorial(int(argv[1])))
  # print(W(int(argv[1]),int(argv[2])) % 1000000007)
  # print(factorCardByPrime(int(argv[1])))
  # print(W2(int(argv[1]),int(argv[2])))
  cardByPrime = factorCardByPrimeFactorial(int(argv[1]))
  print(cardByPrime)
  primeTuples = getPrimeTuples(cardByPrime, int(argv[2]))
  print(len(primeTuples)%1000000007)
