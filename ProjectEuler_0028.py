from sys import argv

# returns the sum of the numbers on the diagonal
# from the bottom left to the top right
def sumDiagBotLftTopRgt(n):
    i=1
    d=4
    s=1
    cnt=1
    while cnt<n:
        for t in range(2):
            i+=d
            cnt+=1
            s+=i
        d+=4
    return s

# returns the sum of teh numbers on the diagonal from the
# bottom right to the top left
def sumDiagBotRgtTopLft(n):
    s=1
    i=1
    d=2
    cnt=1
    while cnt<n:
        cnt+=1
        i+=d
        s+=i
        d+=2
    return s

# returns the sum of the numbers on the diagonals in an nxn
# grid formed by starting with the number 1 in the center
# and moving to the right in a clockwise direction
def getAnswer(n):
    return sumDiagBotRgtTopLft(n) +\
           sumDiagBotLftTopRgt(n) - 1

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
