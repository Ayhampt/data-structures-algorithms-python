'''
concept
-------
suppose we have number 153 to check it is armstrong 153 = 1^3+5^3+3^3 if this is
true then it is armstrong else not 3->number of digits in an integer
'''
from math import log10
n = 153
num = n
def countDigits(num):
  if num==0:
    return 1
  return int(log10(num)+1)


def check_armstrong(num,n):
  if n==0:
    return True
  digit_count = countDigits(n)
  total = 0
  while num > 0:
    last_digit = num%10
    total+=last_digit**digit_count
    num = num//10
  return total == n

print(check_armstrong(num,n))
