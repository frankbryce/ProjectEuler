# returns the sum of all the numbers that can be written as
# the sum of fifth powers of their digits
def getAnswer():
    s=0
    for i in range(600000): # upper bound on the possible answers
        num = "{0:06d}".format(i)
        p=0
        for ch in num:
            p += int(ch)**5
        if p==i:
            print(i)
            s+=i
    return s-1

if __name__=="__main__":
    print(getAnswer())
