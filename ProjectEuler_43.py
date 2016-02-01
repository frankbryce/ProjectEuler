def _strWithoutIdx(s,idx):
  if idx==0:
    return s[1:]
  elif idx==len(s)-1:
    return s[:-1]
  else:
    return s[0:idx]+s[idx+1:len(s)]

def getAnagrams(s):
  if len(s)==1:
    yield s
  else:
    for i in range(len(s)):
      for strs in getAnagrams(_strWithoutIdx(s,i)):
        yield s[i:i+1] + strs

def getStringsMatchingMagicalProperty():
  for s in getAnagrams("0123456789"):
    if int(s[7:10])%17!=0: continue
    if int(s[6: 9])%13!=0: continue
    if int(s[5: 8])%11!=0: continue
    if int(s[4: 7])% 7!=0: continue
    if int(s[3: 6])% 5!=0: continue
    if int(s[2: 5])% 3!=0: continue
    if int(s[1: 4])% 2!=0: continue
    yield s

if __name__=="__main__":
  print(list(getStringsMatchingMagicalProperty()))