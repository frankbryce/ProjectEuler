from iterUtil import tupleRange
from iterUtil import tupleDiff
from iterUtil import maxValuesInTuples
from functools import reduce
import pytest

@pytest.mark.parametrize("t",[(2,3,5),(5,2,3),(5,7,9),(5,2,0)])
def test_tupleRange(t):
  assert len(list(tupleRange(t))) == reduce(lambda x, y: x * (y+1), t, 1)
  
@pytest.mark.parametrize("t",[[(2,3,5),(5,2,3),(5,7,9),(5,2,0)]])
def test_maxValueInTuples(t):
  assert maxValuesInTuples(t) == (5,7,9)

def getTupleRange(t):
  for item in tupleRange(t):
    pass
  
@pytest.mark.parametrize("t",[(1,2,3,4,5,6)])
def test_tupleRangeSpeed(benchmark, t):
  benchmark(getTupleRange, t)
  
def test_tupleDiff():
  assert tupleDiff((3,2,1),(2,1,0))==(1,1,1)
  assert tupleDiff((10,14,12,7,5,3),(8,4,6,5,1,3))==(2,10,6,2,4,0)
