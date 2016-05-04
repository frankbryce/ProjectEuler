
function f(n,a,b)
    return n^2 + a*n + b
end

function isPrime(num)
    if num<2 then return false end
    if num%2==0 then return false end
    for i=3,num/3,2 do
        if num%i==0 then return false end
    end
    return true
end

bign=0
biga=0
bigb=0
for a=-999,999 do
    for b=-999,999 do
        n=0
        while isPrime(f(n,a,b)) do n = n+1 end
        if n>bign then bign=n ; biga=a ; bigb=b end
    end
end
print(biga * bigb)
print(bign)
