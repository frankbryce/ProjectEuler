import functools
  
## where l is the length of the string and n is that size of the alphabet
# q'(l,n) = number of ways to make a permutation of unique characters where exactly 0 characters are larger than its directly left neighbor
# p'(l,n) = number of ways to make a permutation of unique characters where exactly 1 character is larger than its directly left neighbor
#
# p(idx, l,n) = p'(l,n) where idx is the index of the character in the list of sorted characters in the permutation
# q(idx, l,n) = q'(l,n) where idx is the index of the character in the list of sorted characters in the permutation
#
# need to check boundary conditions
# p(idx, l, n) = q([0:idx], l-1, n-1) + p([idx:l-1], l-1, n-1)
# q(idx, l, n) = q([idx:l-1], l-1, n-1)
#
# p(0, 1, n) = 0
# p(0, 2, n) = 0
# p(1, 2, n) = n*(n-1)/2
# q(0, 1, n) = 1
# q(0, 2, n) = n*(n-1)/2
# q(1, 2, n) = 0
#
# check:
#   p(0,3,3) = q(0, 2, 2) = 2*(2-1)/2 = 1 (number of posibilities choosing "a" as first character in anagrams of substrings of "abc" of length 3) (should be 1)
#   p(1,3,3) = q(0, 2, 2) + p(1, 2, 2) = 1 + 2*(2-1)/2 = 2 ("bac", "bca")
#   p(2,3,3) = q(0, 2, 2) + q(1, 2, 2) = 1 + 0 = 1 ("cab")
#   p(0,3,4) = p(0,2,3) + p(1,2,3) = 0 + 3*2/2 = 3 ("adbc", "acbd", "acdb")
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

# debugging helper
def printerDecorator(f):
  def wrapper(*args, **kwargs):
    r = f(*args, **kwargs)
    print(*args, r, sep=",")
    return r
  return wrapper

@listUnroll
@functools.lru_cache(maxsize=None)
@printerDecorator
def p(idx, l, n):
  if idx==0 and l==2:
    return 0
  if idx==1 and l==2:
    return n*(n-1)/2
  sum = 0
  if idx > 0:
    sum += q(range(idx), l-1, n-1)
  if idx<l-1:
    sum += p(range(idx,l-1), l-1, n-1)
  return sum
  
@listUnroll
@functools.lru_cache(maxsize=None)
@printerDecorator
def q(idx, l, n):
  if idx==0 and l==2:
    return n*(n-1)/2
  if idx < l-1:
    return q(range(idx,l-1), l-1, n-1)
  return 0
  
def p_n(l, n):
  return p(range(l),l,n)
  
if __name__ == "__main__":
  print(p_n(3,26))