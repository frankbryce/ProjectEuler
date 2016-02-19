from sys import argv
from primeUtil import getPrimesUpTo

# returns the sum of all primes below n
def getAnswer(n):
    s = 0
    for prime in getPrimesUpTo(n):
        s += prime
    return s

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
