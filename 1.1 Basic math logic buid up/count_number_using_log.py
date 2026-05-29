from math import *
n = 5873
def count_digits(num):
  count = int(log10(num)+1)
  return count
print(count_digits(n))