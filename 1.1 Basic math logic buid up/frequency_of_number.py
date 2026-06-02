"""
Problem : given a list of numbers find the frequency of each number
"""
"""
Method 1:using a dictionary
---------------------------
 iterate through the list nums check if num[i] in dictionary if not add it and set the value to 1 else add the
 value by one
"""
nums = [1,1,2,2,5,4,3,2]
dict = {}
for i in range(0,len(nums)): # O(N)
  if nums[i] in dict:
    dict[nums[i]]+=1 # O(1)
  else:
    dict[nums[i]] = 1 # O(1)
print(dict)

"""Time complexity -> O(N)"""

"""
Method 2 :
----------
hash_map[nums[i]] = hash_map.get(nums[i],0)+1    suppose (nums[i],0)+1 - > 5,0 this means
when the value 5 not in the hash_map return 0 else add 1 to it
"""
hash_map = {}
for i in range(0,len(nums)):
  hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)