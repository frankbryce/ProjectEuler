from sys import argv
import primeUtil

# primeSums[sum] = the number of subsets of the
# nums list that add up to sum
def getPrimeSums(nums):
  primeSums = {}
  primeSums[0] = 1
  for num in nums:
    for sum in list(primeSums)[::-1]:
      if sum+num not in primeSums:
        primeSums[sum+num] = 0
      primeSums[sum+num] += primeSums[sum]
  return primeSums
  
def getCountOfSumsOfPrimeSubsets(upTo):
  primes = primeUtil.getPrimesUpTo(upTo)
  primeSums = getPrimeSums(primes)
  count=0
  for sum in primeSums:
    if primeUtil.isPrime(sum):
      count += primeSums[sum]
  print(primeSums)
  return count

if __name__=="__main__":
  print(getCountOfSumsOfPrimeSubsets(int(argv[1])))