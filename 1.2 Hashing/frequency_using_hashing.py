"""Problem : given two list n and m
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
with constrains 1<=n[i]<=10
n has 10^8 elements
m has 10^8 elements
check the frequency of elements of m in n
"""

""""
Method 1 : using List hashing
----------------------------
what is hashing ? (pre storing values into some data structure like list/dict and fetching it)
how do we do it ? :
create a list of len of 11 [0]*11 as it is given 1<=n[i]<=10 and by default value 0 in every index
then iterate through the list n and increment 1 in the new list where the index == n[i] in the list n
"""

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
lst = []
hash_map = [0]*11
for i in n:
  hash_map[i]+=1
print(hash_map)
for num in m:
  if num<1 or num>10:
    lst.append(0)
  else:
   lst.append(hash_map[num])
print(lst)

"""Time complexity -> O(m+n)
  space complexity -> O(11) = O(1)
"""

"""
Method 2 : using dictionary
---------------------------
how do we do it ?:
algorithm :

iteration 1:
----------
k = 5
hash_map[5] = hash_map.get(5,0)+1
hash_map.get(5,0) if the 5 not exist return 0 else return value from dictionary
so, hash_map[5] = 0+1
{5:1}

----------
"""
hash_map = {}
for k in n:
  hash_map[k] = hash_map.get(k,0)+1
freq_of_m = []
for num in m:
  if num<1 or num>10:
    freq_of_m.append(0)
  else:
    freq_of_m.append(hash_map.get(num,0))
print(freq_of_m)

"""Time complexity -> O(m+n)"""