from sys import argv

# returns the last 10 digits of the series
# 1**1 + 2**2 + ... + n**n
def getAnswer(n):
    s=0
    for i in range(1,n+1):
        s += (i**i)
    return str(s)[-10:]

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
