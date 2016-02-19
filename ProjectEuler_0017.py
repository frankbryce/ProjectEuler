from sys import argv
import functools

# returns the number of letters in the positive integer n
@functools.lru_cache(maxsize=1024)
def numLetters(n):
    if n<20:
        if n==0: return 0 # to handle recursion
        if n==1 or n==2 or n==6 or n==10: return 3
        if n==4 or n==5 or n==9: return 4
        if n==3 or n==7 or n==8: return 5
        if n==11 or n==12: return 6
        if n==15 or n==16: return 7
        if n==13 or n==14 or n==18 or n==19: return 8
        if n==17: return 9
    if n<30: return 6+numLetters(n%10)
    if n<40: return 6+numLetters(n%10)
    if n<50: return 5+numLetters(n%10)
    if n<60: return 5+numLetters(n%10)
    if n<70: return 5+numLetters(n%10)
    if n<80: return 7+numLetters(n%10)
    if n<90: return 6+numLetters(n%10)
    if n<100: return 6+numLetters(n%10)
    if n<1000:
        ltrs=7 #hundred
        if n%100!=0: ltrs+=3 #and
        return numLetters(int(n/100))+ltrs+numLetters(n%100)
    if n==1000: return 11
    raise ValueError("n must be an integer between 1 and 1000")

# gets the number of letters that would be used if the numbers from 1
# through the positive integer n were written out in words
def getAnswer(n):
    s = 0
    for i in range(1,n+1):
        s += numLetters(i)
    return s

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
