from sys import argv

# generator for fibonacci numbers
def getFibs():
    f1, f2 = 0, 1
    while True:
        yield f1
        f1, f2 = f2, f1+f2

# returns the first term in the fibonacci sequence
# to contain n digits
def getAnswer(n):
    idx=0
    for fib in getFibs():
        if len(str(fib))>=n: return idx
        idx += 1

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
