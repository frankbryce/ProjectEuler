import functools
from random import shuffle

def iterThrough(lists):
  if not hasattr(lists[0], '__iter__'):
    for val in lists:
      yield val
  else:
    for l in lists:
      for val in iterThrough(l):
        yield val

def tupleDiff(t1, t2):
  return tuple(x-y for x,y in zip(t1,t2))

def maxValuesInTuples(l):
  ret = [0]*len(l[0])
  for tup in l:
    for idx in range(len(tup)):
      ret[idx] = max(tup[idx],ret[idx])
  return tuple(ret)

def tupleRange(l, startAt=None):
  if len(l)==1:
    if startAt==None:
      rg = range(l[0]+1)
    else:
      rg = range(startAt[0],l[0]+1)
    for i in rg:
      yield tuple([i])+l[1:]
  else:
    if startAt==None:
      rg = range(l[0]+1)
    else:
      rg = range(startAt[0],l[0]+1)
      startAt = startAt[1:]
    l = l[1:]
    for l2 in tupleRange(l, startAt):
      for i in rg:
        yield tuple([i])+l2

if __name__ == '__main__':
  for val in iterThrough(
    [[[111,112,113],[121,122,123],[131,132,133]],
     [[211,212,213],[221,222,223],[231,232,233]],
     [[311,312,313],[321,322,323],[331,332,333]]]):
    print(val)
  for d in tupleRange((7,6,5,4,3)):
    print(d)