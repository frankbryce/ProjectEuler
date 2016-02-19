from sys import argv
import functools

# returns the length of the Collatz sequence starting at n
@functools.lru_cache(maxsize=2000000)
def lenCollatz(n):
    if n<1: raise ValueError("n must be a positive integer")
    if n==1: return 1
    if n%2==0: return 1+lenCollatz(int(n/2))
    return 1+lenCollatz(3*n+1)

# returns the starting number of, and the length of, the longest Collatz sequence
# which starts at a number below n
def getAnswer(n):
    mx = 1
    mxStart = 1
    for i in range(2,n):
        l = lenCollatz(i)
        if l > mx:
            mx = l
            mxStart = i
    return mxStart, mx

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
