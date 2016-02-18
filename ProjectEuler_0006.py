from sys import argv

# gets the first n perfect squares
def getSquares(n):
    for i in range(1,n+1):
        yield i*i

def sumOfFirstNNumbers(n):
    return int(n*(n+1)/2)

# returns the difference between the sum of the squares
# of the first one hundred natural numbers and the
# square of their sum
def getAnswer(n):
    s=0
    for i in getSquares(n):
        s += i
    return sumOfFirstNNumbers(n)**2 - s

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
