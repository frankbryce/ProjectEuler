from sys import argv

# returns the sum of all the multiples of 3
# or 5 below n
def getAnswer(n):
    s = 0
    for i in range(n):
        if i%3==0 or i%5==0:
            s += i
    return s

if __name__=="__main__":
     print(getAnswer(int(argv[1])))

