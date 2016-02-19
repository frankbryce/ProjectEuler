from sys import argv
import math

# returns the sum of the digits in n factorial
def getAnswer(n):
    nFact = math.factorial(n)
    s = 0
    for ch in str(nFact):
        s += int(ch)
    return s

if __name__=="__main__":
    print(getAnswer(int(argv[1])))

