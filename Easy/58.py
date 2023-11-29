#Length of Last Word
#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.

s = "Hello World"
res = s.split()
print(len(res[-1]))

