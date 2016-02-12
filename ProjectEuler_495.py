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

def getTupleCount(cards, ofLength):
    if ofLength==1:
        return 1
    if len(cards)==2 and ofLength==2:
        if cards[0]==0:
            if cards[1]%2==0:
                return int(cards[1]/2)
            return int((cards[1]+1)/2)
        if cards[0]==1:
            return cards[1]+1
        if cards[0]%2==1:
            cards = list(cards)
            cards[0] = int(cards[0]/2)
            return 2*int(getTupleCount(tuple(cards),ofLength))
        if cards[0]%2==0:
            cards1 = list(cards)
            cards2 = list(cards)
            cards1[0] = int(cards[0]/2)
            cards2[0] = int(cards[0]/2)-1
            return getTupleCount(cards1,ofLength)+getTupleCount(cards2,ofLength)
    return 1 + getTupleCount(cards,ofLength-1)

if __name__=="__main__":
    print("      ",end="")
    for i in range(9):
        print("  "+str(i)+"  ", end=" ")
    print()
    setsDone=set()
    for i in range(20):
        print('{0: =5d} '.format(i), end=" ")
        for j in range(9):
            tup = (i,j)
            #if tuple(sorted(tup)) in setsDone: continue
            setsDone.add(tuple(sorted(tup)))
            print('{0: =5d}'.format(getTupleCount(tuple(sorted(tup)), 2)), end=" ")
        print()
    
