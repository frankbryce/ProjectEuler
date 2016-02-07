def iterThrough(lists):
  if not hasattr(lists[0], '__iter__'):
    for val in lists:
      yield val
  else:
    for l in lists:
      for val in iterThrough(l):
        yield val


def dictIterDecorator(dIter):
  dIterCache = {}
  def dictIterCache(d):
    cIdx = tuple(list(d.keys())+list(d.values()))
    if cIdx not in dIterCache:
      dIterCache[cIdx] = list(dIter(d))
    return dIterCache[cIdx]
  return dictIterCache

@dictIterDecorator
def dictIter(d):
  keys = list(d.keys())
  if len(keys)==1:
    n = d[keys[0]]
    for i in range(n+1):
      d[keys[0]]=i
      yield d
  else:
    d2 = d.copy()
    del d2[keys[0]]
    for d2s in dictIter(d2):
      for i in range(d[keys[0]]+1):
        d2s[keys[0]] = i
        yield d2s

if __name__ == '__main__':
  for val in iterThrough(
    [[[111,112,113],[121,122,123],[131,132,133]],
     [[211,212,213],[221,222,223],[231,232,233]],
     [[311,312,313],[321,322,323],[331,332,333]]]):
    print(val)
  for d in dictIter({2:5,3:4,4:3}):
    print(d)