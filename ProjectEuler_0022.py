# returns the alphabetical position of the letter l
# a=A=1, b=B=2, ..., z=Z=26
def indexOf(l):
    return ord(l.lower())-96

# returns the sum of the name scores in the list of names
# names is a list of strings, and the score of a name in the
# list is the alphabetical position of the name in the list
# multiplied by the sum of the alphabetical position of each
# letter in the name.  (a=1, z=26)
def getAnswer(names):
    sNames = sorted(names)
    s=0
    for i in range(len(sNames)):
        t=0
        for ch in sNames[i]:
            t += indexOf(ch)
        s += (t*(i+1))
    return s

if __name__=="__main__":
    with open("ProjectEuler_0022.input.txt") as f:
        names = f.read().replace("\"","").split(',')
    print(getAnswer(names))
