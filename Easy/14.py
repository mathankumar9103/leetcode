#Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
strs = ["flower","flow","flight"]

out = ''

first_item = strs[0]
lst = strs[1:]
brk = 0

for itr in first_item:
    for itr1 in lst:
        cnt = out + itr
        if cnt == itr1[:len(cnt)]:
            pass
        else:
            brk = 1
            break
    if brk == 1:
        break
    else:
        out = out + itr
print(out)

out = ''

first_item = strs[0]
lst = strs[1:]
brk = 0
for itr in first_item:
    for itr1 in lst:
        cnt = out + itr
        if cnt == itr1[:len(cnt)]:
            pass
        else:
            brk = 1
            break

    if brk == 1:
        break

    else:
        out = out + itr

print(out)