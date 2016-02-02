from itertools import tee
from pdb import set_trace
import functools

class _state:
  def __init__(self):
    self.lastSum = {}
    self.sumGenerators = {}
    
  def getPK(self):
    def naturalGetter():
      i=0
      while True:
        i += 1;
        yield i
        
    kGetter = naturalGetter()
    while True:
      k=next(kGetter)
      #set_trace()
      idx=0
      foundPK = False
      while not foundPK:
        idx += 1
        if idx in self.lastSum:
          if k in self.lastSum[idx]:
            yield idx; break
          elif k < self.lastSum[idx][-1]:
            continue
        sums = getSumGetter(idx,self)
        for sum in sums:
          if sum==k:
            foundPK = True;
            yield idx;
            break
          elif sum>k:
            break

def sumGetter(idx, state):
  getter = getDigitGetter(idx)
  sum = 0
  for d in getter:
    if d != 0:
      sum += d
      if idx in state.lastSum:
        state.lastSum[idx].append(sum)
        if len(state.lastSum[idx])>10: state.lastSum[idx].pop(0)
      else:
        state.lastSum[idx] = [sum]
      yield sum

def getSumGetter(idx, state):
  if idx in state.sumGenerators:
    return state.sumGenerators[idx]
  state.sumGenerators[idx] = sumGetter(idx, state)
  return state.sumGenerators[idx]

def getDigitGetter(idx):
  getter = getDigits()
  for i in range(idx-1):
    next(getter)
  return getter
  
def getDigits():
  def getNextNumber(n):
    return (n*n) % 20300713

  s0 = s = "14025256"
  while True:
    for ch in s: yield int(ch)
    s = str(getNextNumber(int(s)))
    if s == s0: break
      
def calculateSumOfPksUpTo(n):
  sum = 0
  found = 0
  state = _state()
  for pk in state.getPK():
    found += 1
    sum += pk
    if found==n: return sum


def calculateSumOfPks():
  return calculateSumOfPksUpTo(2*10**15)

if __name__=="__main__":
  print("sum(p(k)), for 0<k<=10^3 = " + str(calculateSumOfPksUpTo(10**3)))
  #print("sum(p(k)), for 0<k<=2*10^15 = " + str(calculateSumOfPks()))