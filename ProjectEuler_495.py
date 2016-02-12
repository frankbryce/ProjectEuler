from math import sqrt,factorial
from primeUtil import getPrimesUpTo
from iterUtil import tupleRange
from iterUtil import tupleDiff
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
  
@functools.lru_cache(maxsize=256)
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

@functools.lru_cache(maxsize=65536)
def getTuples(cards, notIn, ofLength):
  if ofLength==1:
    if cards not in notIn:
      return 1
    return 0
  else:
    cnt=0
    for tup in tupleRange(cards):
      if tup not in notIn:
        notIn = notIn.union([tup])
        cnt += getTuples(tupleDiff(cards,tup), notIn, ofLength-1)
    return cnt
    
if __name__=="__main__":
  # cardByPrime = factorCardByPrimeFactorial(int(argv[1]))
  # cardByPrime = factorCardByPrime(int(argv[1]))
  # print(cardByPrime)
  # print(getTuples(tuple(cardByPrime.values()), frozenset(), int(argv[2])))
  print("          ", end=" ")
  for i in range(1,10):
    print("  "+str(i)+"  ", end=" ")
  print()
  setsDone=set()
  for tup in tupleRange((5,5,5)):
    if frozenset(tup) in setsDone: continue
    setsDone.add(frozenset(tup))
    print(tup[::-1], end=": ")
    for card in range(1,10):
      print('{0: =5d}'.format(getTuples(tup,frozenset(), card)), end=" ")
    print()
    