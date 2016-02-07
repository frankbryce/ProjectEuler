import pytest
from ProjectEuler_495 import factorCardFactorial

@pytest.mark.parametrize("n",[(2,1),(3,2),(5,5),(10,15)])
def test_factorialFactoringCardinality(n):
  assert factorCardFactorial(n[0])==n[1]