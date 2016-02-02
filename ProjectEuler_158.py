import functools
  
#### l is the length of the string and n is that size of the alphabet
# q'(l,n) = number of ways to make a permutation of unique characters where exactly 0 characters are larger than its directly left neighbor
# p'(l,n) = number of ways to make a permutation of unique characters where exactly 1 character is larger than its directly left neighbor
#
# p(idx, l,n) = p'(l,n) where idx is the index of the character in the list of n sorted characters
# q(idx, l,n) = q'(l,n) where idx is the index of the character in the list of n sorted characters
#
# need to check boundary conditions
# p(idx, l, n) = q([0:idx], l-1, n-1) + p([idx:n-1], l-1, n-1)
# q(idx, l, n) = q([idx:n-1], l-1, n-1)
def listUnroll(f):
  def wrapper(idxs, *args):
    if type(idxs)==range:
      idxs = list(idxs)
    if type(idxs)==list:
      sum = 0
      for idx in idxs:
        sum += f(idx, *args)
      return sum
    else:
      return f(idxs, *args)
  return wrapper

@functools.lru_cache(maxsize=None)
@listUnroll
@functools.lru_cache(maxsize=None)
def p(idx, l, n):
  assert 0<=idx and idx<n
  if l<=2:
    return idx
  sum = q(range(idx), l-1, n-1) + \
        p(range(idx,n-1), l-1, n-1)
  return sum
  
@functools.lru_cache(maxsize=None)
@listUnroll
@functools.lru_cache(maxsize=None)
def q(idx, l, n):
  assert 0<=idx and idx<n
  if l==1:
    return 1
  if l==2:
    return n-1-idx
  return q(range(idx,n-1), l-1, n-1)
  
def p_n(l, n=26):
  return p(range(n),l,n)
  
if __name__ == "__main__":
  pns = [p_n(n) for n in range(26)]
  mx = max(pns)
  print("n=",pns.index(mx), ", p(n)=",mx,sep="")