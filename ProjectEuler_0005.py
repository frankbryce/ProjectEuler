from sys import argv
from primeUtil import factorCardByPrime

# returns the smallest positive number that is evenly divisible
# by all of the numbers from 1 to n
def getAnswer(n):
    cards = {}
    for i in range(2,n+1):
        c = factorCardByPrime(i)
        for prime in c:
            if prime not in cards or c[prime]>cards[prime]:
                cards[prime]=c[prime]

    p=1
    for i in cards:
        p *= i**cards[i]
    return p

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
