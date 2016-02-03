from sys import argv
from math import sqrt
from pdb import set_trace

def isPrime(n):
  for i in getPrimesUpTo(int(sqrt(n))):
    if n%i==0: return False
  return True

def getPrimesUpTo(n):
  yield 2; yield 3
  if n<=3: return
  for i in list(range(n+1))[3::2]:
    if isPrime(i): yield i

def getPrimeSubsetSumsUpTo(n):
  pass

if __name__=="__main__":
  ps = list(getPrimesUpTo(int(argv[1])))
  print(ps)
  print(len(ps))