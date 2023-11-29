#Find the Index of the First Occurrence in a String

#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# haystack = "sadbutsad"
# needle = "sad"
haystack = "leetcode"
needle = "leet"
for itr in haystack:
    if needle in haystack:
        res = haystack.find(needle)
    else:
        res = -1
print(res)















lack = ""