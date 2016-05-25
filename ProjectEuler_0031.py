from sys import argv
from functools import lru_cache
import timeit

coins = (1,2,5,10,20,50,100,200)

def pyAnswer(pence):
  if pence==0: return 1
  coinCounts = tuple([0 for c in coins])
  coinSets = set()
  
  def addToSet(i, p, c, s):
    if p >= c:
      answers = recurse(p-c)
      for ans in answers:
        ansList = list(ans)
        ansList[i] += 1
        s.add(tuple(ansList))
  
  @lru_cache(maxsize=256)
  def recurse(pence):
    if pence==0: return set([tuple([0 for c in coins])])
    coinSets = set()
    for i, coin in enumerate(coins):
      addToSet(i, pence, coin, coinSets)
    return coinSets
    
  for i,coin in enumerate(coins):
    addToSet(i, pence, coin, coinSets)
  return len(coinSets)
  
@lru_cache(maxsize=256)
def goAnswer(pence):
  # todo
  return "golang answer"

if __name__=="__main__":
  pence = argv[1]
  print(pyAnswer(int(pence)))
  print(goAnswer(int(pence)))
  print(timeit.repeat("pyAnswer("+pence+")", "from __main__ import pyAnswer", number=2))
  print(timeit.repeat("goAnswer("+pence+")", "from __main__ import goAnswer", number=2))