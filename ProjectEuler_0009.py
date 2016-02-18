from sys import argv
from math import sqrt

# returns True if n is a perfect square, False otherwise
def isPerfectSquare(n):
    return int(sqrt(n))**2==n

# returns the product of the pythagorean triplet of numbers
# a*b*c such that a^2*b^2=c^2 and a+b+c==n.  If it fails to
# find a triplet with such a property, then it returns -1
def getAnswer(n):
    for a in range(1,n):
        for b in range(a+1,n):
            c = n-a-b
            if a*a+b*b != c*c: continue
            return a*b*c
    return -1

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
