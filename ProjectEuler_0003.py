from sys import argv
from primeUtil import factorCardByPrime

# returns the largest prime factor of the number n
def getAnswer(n):
    cards = factorCardByPrime(n)
    return sorted(list(cards))[-1]

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
