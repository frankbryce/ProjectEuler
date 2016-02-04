from primeUtil import getPrimesUpTo
import pytest

@pytest.mark.parametrize("n",[(1000,168)])
def test_itGetsAllPrimes(n):
  assert len(list(getPrimesUpTo(n[0])))==n[1]
  
@pytest.mark.parametrize("n",[(2,2),(3,3),(4,3),(1000,997),(10000,9973)])
def test_itGetsCorrectPrimes(n):
  assert list(getPrimesUpTo(n[0]))[-1]==n[1]
  
@pytest.mark.parametrize("n",[10,1000,10000])
def test_itsFastToo(benchmark, n):
  benchmark(getPrimesUpTo, n)