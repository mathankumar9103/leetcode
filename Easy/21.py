# Merge Two Sorted Lists
#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

list1 = [1,2,4]
list2 = [1,3,4]
for itr in list2:
    list1.append(itr)
print(sorted(list1))
