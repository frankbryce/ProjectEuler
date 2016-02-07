from iterUtil import dictIter
from functools import reduce
import pytest

@pytest.mark.parametrize("d",[{2:2,3:3,5:5}, {2:5,3:2,5:3},{2:5,3:7,5:9}, {2:5,3:2,5:0}])
def test_dictIter(d):
  assert len(list(dictIter(d))) == reduce(lambda x, y: x * (y+1), list(d.values()), 1)

def getDictList(d):
  for item in dictIter(d):
    pass
  
@pytest.mark.parametrize("d",[{2:2,3:3,5:4,7:5,11:6,13:7},{2:2,3:3,5:4,7:5,11:6,13:7,17:8},{2:2,3:3,5:4,7:5,11:6,13:7,17:8,19:9},{2:2,3:3,5:4,7:5,11:6,13:7,17:8,19:9,23:10}])
def test_dictIterSpeed(benchmark, d):
  benchmark(getDictList, d)