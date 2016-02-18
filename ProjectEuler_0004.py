from sys import argv

# returns True if the positive integer n is a palidrome,
# and False otherwise
def isPalindrome(n):
    nstr = str(n)
    return nstr==nstr[::-1]

# returns the largest palindrome made from the product of
# two n-digit numbers
def getAnswer(n):
    mx = int('9'*n)
    mxPr = 1
    for i in range(1,mx+1):
        for j in range(1,i+1):
            if i*j>mxPr and isPalindrome(i*j):
                mxPr=i*j
    return mxPr

if __name__=="__main__":
    print(getAnswer(int(argv[1])))
