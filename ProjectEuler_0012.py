from sys import argv
from primeUtil import factorCardByPrime

# generator for the triangle numbers
def getTriangleNums():
    i=0
    s=0
    while True:
        i+=1
        s+=i
        yield s

# returns the value of the first triangle number to have
# over n divisors
def getAnswer(n):
    for num in getTriangleNums():
        cards = factorCardByPrime(num)
        divs = 1
        for card in cards:
            divs *= (cards[card]+1)
        if divs > n:
            return num

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
