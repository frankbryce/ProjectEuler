from itertools import tee
from pdb import set_trace
import functools

class _state:
  def __init__(self):
    self.lastSum = {}
    
  def getPK(self):
    k=1
    idx=0
    while True:
      idx+=1
      if idx in self.lastSum:
        if k <= self.lastSum[idx][-1]:
          if k in self.lastSum[idx]:
            yield idx; idx=0; k+=1
          continue
      for sum in self.sumGetter(idx):
        if sum==k: yield idx; idx=0; k+=1; break
        elif sum>k: break

  @functools.lru_cache(maxsize=None)
  def sumGetter(self, idx):
    sum = 0
    for d in self.getDigitGetter(idx):
      if d != 0:
        sum += d
        if idx in self.lastSum:
          self.lastSum[idx].append(sum)
          if len(self.lastSum[idx])>10: self.lastSum[idx].pop(0)
        else:
          self.lastSum[idx] = [sum]
        yield sum

  @functools.lru_cache(maxsize=None)
  def getDigitGetter(self, idx):
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