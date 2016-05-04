function primes(upto)
    upto = upto or 10
    local prime=1
    return function()
        if prime==1 then prime = 2 ; return prime end
        local nxt = prime
        if nxt>=upto then return nil end        
        repeat
            nxt = nxt + 1
            local isprime = true
            for p=2,prime do
                if nxt%p == 0 then isprime=false ; break end
            end
        until isprime or nxt>=upto
        if nxt>=upto then return nil end
        prime = nxt
        return prime
    end
end

function primefactors(n)
    local fs={}
    for prime in primes(n/2) do
        if n%prime==0 then
            if not fs[prime] then
                fs[prime] = 1
            else
                fs[prime] = fs[prime] + 1
            end
            n = n/prime
        end
    end
    return fs
end

function factors( n ) 
    local f = {}
 
    for i = 1, n/2 do
        if n % i == 0 then 
            f[#f+1] = i
        end
    end
    --f[#f+1] = n
 
    return f
end

function isAbundant(n)
    local s=0
    for _,v in ipairs(factors(n)) do
        s = s + v
    end
    return s > n
end

function abundants(upto)
    local a=1
    return function()
        if a==1 then a=12 ; return a end
        while a<upto do
            a = a + 1
            if isAbundant(a) then return a end
        end
        return nil
    end
end

abunds = {}
for a in abundants(28123) do
    table.insert(abunds, a)
end

ans={}
for i = 1,28123 do ans[i]=0 end

for _,i in ipairs(abunds) do
    for _,j in ipairs(abunds) do
        ans[i+j]=1
    end
end

s=0
for i,v in ipairs(ans) do
    if v==0 then s = s + i end
end

print (s)
