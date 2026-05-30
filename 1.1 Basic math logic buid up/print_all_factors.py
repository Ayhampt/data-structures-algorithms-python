"""
Method 1 : brute force
----------------------
with time Complexity of O(N),space complexity O(k) k->number of factors of
number
"""
num = 20
result = []
for i in range(1,num+1):
  if num%i == 0:
    result.append(i)
print(result)

"""
Method 2 : Better solution
---------------------------
if we look into a number suppose 20 the factors are [1, 2, 4, 5, 10, 20] we only
want to iterate from 1 to half of the 20 which is 10 the numbers after 10 to 19
cannot be factor yes 20 is the factor
"""
sol = []
for j in range(1,num//2+1):
  if num%j==0:
    sol.append(j)
sol.append(num)
print(sol)

"""
Time complexity -> O(N/2) = O(N)
Space complexity -> O(k)
"""

"""
Method 3 : Optimal Solution
---------------------------
if the given number os 36 we can see when we start from 1 to check for factors
divide the factor from the num example:36/factor
gives another factor
for example 36//1 gives 36 which is another factor
1 - 36
2 - 18
3 - 12
4 - 9
6 - 6
in this solution we dont have to go look from 1 to 36 just sqrt(num)
"""
from math import sqrt
best_result = []
for k in range(1,int(sqrt(num))+1):
  if num%k == 0:
    best_result.append(k)
    if num//i != i:
      best_result.append(num//k)
print(best_result)

"""
Time Complexity -> O(sqrt(n))
"""