Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
value = "MCMXCIV"
res = 0
prev = 0
for idx,itr in enumerate(value):
    if idx != 0:
        if roman[itr] > prev:
            res = res - prev + roman[value[idx]] - roman[value[idx-1]]
        else:
            res = res + roman[itr]
            prev = roman[itr]
    else:
        res = roman[itr]
        prev = res

print(res)









