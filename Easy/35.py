#Search Insert Position
#Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# nums = [1,3,5,6]
# target = 5
#
# for itr in range(len(nums)):
#     if nums[itr] == target:
#         print(itr)
# else:
#     nums.append(target)
#     a = sorted(nums)
#     for itr1 in range(len(a)):
#         if nums[itr1] == target:
#             print(itr1)


#updated code
# nums = [1,3,5,6]
# target = 7
#
# if target in nums:
#     print(nums.index(target))
# else:
#     nums.append(target)
#     a = nums.sort()
#     print(nums.index(target))








# x = int(input("enter X:"))
# n = int(input("enter n:"))
# count = 2
# res = 0
# for itr in range(1,n+1):
#     out = x ** count
#     res = res + out
#     count += 2
# print(res)




# x = int(input("enter x:"))
# n = int(input("enter n:"))
# count = 2
# res = 0
# res1 = 0
# res2 = 0
# for itr in range(1,n+1):
#     if (itr%2 == 0):
#         out = -x ** count
#         res1 = res1 + out
#         count += 2
#     else:
#         out = x ** count
#         res2 = res2 + out
#         count += 2
# res = res1 + res2
# print(res)



#
# n = int(input())
# for a in range(n,0,-1):
#     print((" "*(a-1))+("*"*(n-a+1)))



