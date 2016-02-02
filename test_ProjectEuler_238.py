from ProjectEuler_238 import calculateSumOfPksUpTo
import pytest

@pytest.mark.parametrize("n",
  [(10,60),
   (10**2,581),
   (10**3,4742),
   (10**4,49541),
   (10**5,496317),
   (10**6,4969211)])
def test_values(n):
  assert calculateSumOfPksUpTo(n[0]) == n[1]
  
@pytest.mark.parametrize("n",[10**2,10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10,10**11,10**12,10**13,10**14,2*10**15])
def test_bench(benchmark, n):
  benchmark(calculateSumOfPksUpTo, n)
