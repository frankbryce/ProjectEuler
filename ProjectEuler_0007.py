from sys import argv
from primeUtil import getPrimesUpTo

# returns the nth prime number
def getAnswer(n):
    cnt=1
    getPrimes = getPrimesUpTo(float('inf'))
    while cnt<n:
        cnt+=1
        next(getPrimes)
    return next(getPrimes)

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
