#9. sum
#Given an integer x, return true if x is a palindrome, and false otherwise.
x = int(input("Enter the value:"))
s = str(x)
rev = s[::-1]
if s == rev:
    print("True")
else:
    print("False")
