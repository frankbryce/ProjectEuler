from sys import argv
from functools import lru_cache
from primeUtil import factorCardByPrime
from iterUtil import tupleRange
import pdb

# returns the sum of the divisors of n
@lru_cache(maxsize=65536)
def d(n):
    s=0
    primeCards = factorCardByPrime(n)
    primes = list(primeCards)
    cards = tuple([primeCards[prime] for prime in primes])
    for divCard in tupleRange(cards):
        div=1
        for i in range(len(divCard)):
            div *= primes[i]**divCard[i]
        if div!=n:
            s += div
    return s

# generator for amicable numbers where an amicable number
# is one where n==d(d(n)) and n!=d(n)
def getAmicables():
    i=2
    while True:
        if i==d(d(i)) and i!=d(i):
            yield i
        i+=1

# returns the sum of all the amicable numbers under 10000 where
# an amicable number is one where n==d(d(n)) and n!=d(n)
def getAnswer(n):
    s = 0
    for i in getAmicables():
        if i>n: break
        s += i
    return s


if __name__=="__main__":
    print(getAnswer(int(argv[1])))
