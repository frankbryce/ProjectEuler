from sys import argv
from functools import lru_cache

# returns the sum of all Fibonacci numbers at or below n
def getAnswer(n):
    s = 0
    f1, f2 = 0, 1
    while f1<=n:
        if f1%2==0:
            s += f1
        f1, f2 = f2, f1+f2
    return s

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
