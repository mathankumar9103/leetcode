#Remove Duplicates from Sorted Array
#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
nums = [0,0,1,1,1,2,2,3,3,4]

count = 0
for itr in nums:
    if count < 1 or itr > nums[count - 1]:
        nums[count] = itr
        count += 1
print(count)
