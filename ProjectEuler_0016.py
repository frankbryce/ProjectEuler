from sys import argv

# returns the sum of the digits of the number 2**n
def getAnswer(n):
    numStr = str(2**n)
    s=0
    for ch in numStr:
        s += int(ch)
    return s

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
