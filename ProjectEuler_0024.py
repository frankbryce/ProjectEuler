from sys import argv

def getOrderedPerms(tup):
    if len(tup)<=1:
        yield tup
    else:
        sl = sorted(list(tup))
        for i in range(len(sl)):
            for subl in getOrderedPerms(tuple(sl[:i]+sl[i+1:])):
                yield tuple([sl[i]] + list(subl))

# returns the nth lexicographic permutation of the
# integers in the list l
def getAnswer(l,n):
    idx=0
    for perm in getOrderedPerms(tuple(l)):
        idx+=1
        if idx==n: return perm

if __name__=="__main__":
    print(getAnswer([int(x) for x in list(argv[1])], int(argv[2])))
