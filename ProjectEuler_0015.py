from sys import argv
import functools

# returns the number of routes through an nxm grid
@functools.lru_cache(maxsize=1024)
def numRoutes(n,m):
    if n==0 or m==0: return 1
    return numRoutes(n,m-1) + numRoutes(n-1,m)

# returns the number of routes there are through a nxn grid
def getAnswer(n):
    return numRoutes(n,n)

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
