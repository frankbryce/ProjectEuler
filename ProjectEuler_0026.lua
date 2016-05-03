#!/usr/bin/lua

getmetatable('').__index = function(str,i) return string.sub(str,i,i) end

local bc = require "bc"
bc.digits(100000)

maxd = 1
maxper = 1
for d = 1,1000 do
	period = 1
	s = bc.tostring(bc.number(1)/bc.number(d))
	for p = 1,10000 do
		good = true
		for j = 0,p-1 do
			for i = 1,9 do
				if s[#s-j-((i-1)*p)] ~= s[#s-j-(i*p)] then
					good = false
					break
				end
			end
			if not good then break end
		end
		if good then period=p ; break end
	end
	if period > maxper then
		maxper, maxd = period, d
	end
end

print(maxd)
print(maxper)
