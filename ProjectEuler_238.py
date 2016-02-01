from itertools import tee
from pdb import set_trace

def getNextNumber(n):
  return (n*n) % 20300713
  
digitGetters = []
def getCachedDigitGetters(idx, getDigitGetter):
  if idx-1 < len(digitGetters):
    return digitGetters[idx-1]
  elif idx-1 == len(digitGetters):
    return next(getDigitGetter)
  else:
    raise ValueError("cannot get further ahead than next digitGetter")

def getDigitGetters():
  digitGetters.append(getDigits())
  yield digitGetters[-1]
  it = getDigits()
  for d in it:
    _, it2 = tee(it)
    digitGetters.append(it2)
    yield it2
  
def getDigits():
  s0 = s = "14025256"
  while True:
    for ch in s:
      yield int(ch)
    s = str(getNextNumber(int(s)))
    if s == s0:
      break;
      
def calculateSumOfPksUpTo(n):
  def shrink_gap(idx):
    nonlocal p_k, min_k, p_k_sum, max_sz_p_k, num_found
    getter = getCachedDigitGetters(idx, getDigitGetter)
    sum = 0
    for d in getter:
      if d != 0:
        sum += d
        if sum > n: break
        if sum == min_k+1:
          set_trace()
          num_found += 1
          p_k.add(sum)
          while min_k+1 in p_k:
            if min_k in p_k:
              p_k.remove(min_k)
            min_k += 1
          p_k_sum += idx
          if len(p_k) <= max_sz_p_k/2:
            return min_k
          if num_found == n: break
        elif sum > min_k+1:
          return shrink_gap(idx+1)
    
  p_k = set()
  p_k_sum = 0
  min_k = 0
  max_k = 0
  max_sz_p_k = 10
  num_found = 0
  idx = 1
  getDigitGetter = getDigitGetters()
  while (len(p_k)<n):
    getter = getCachedDigitGetters(idx, getDigitGetter)
    sum = 0
    for d in getter:
      if d != 0:
        sum += d
        if sum > n: break
        if sum > min_k and sum not in p_k:
          set_trace()
          num_found += 1
          p_k.add(sum)
          if sum > max_k:
            max_k = sum
          while min_k+1 in p_k:
            if min_k in p_k:
              p_k.remove(min_k)
            min_k += 1
          p_k_sum += idx
          if len(p_k) == max_sz_p_k:
            min_k = shrink_gap(idx)
          if num_found == n: break
            
    if num_found == n: break
    idx += 1
  return p_k_sum

def calculateSumOfPks():
  return calculateSumOfPksUpTo(2*10**15)

if __name__=="__main__":
  print("sum(p(k)), for 0<k<=10^3 = " + str(calculateSumOfPksUpTo(10**3)))
  #print("sum(p(k)), for 0<k<=2*10^15 = " + str(calculateSumOfPks()))