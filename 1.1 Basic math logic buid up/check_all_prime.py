"""
Given a number n, determine whether it is a prime number or not.
Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
"""
from math import sqrt
def is_prime(n):
  if n<=1:
    return False
  if n<=3:
    return True

  if n%2==0 or n%3==0:
    return False

  for i in range(5,int(sqrt(n))+1,6):
    if n%i==0 or n%(i+2)==0:
      return False
    else:
      return True
  return True

print(is_prime(10))