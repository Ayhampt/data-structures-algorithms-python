''' given the input 5873 extract each numbers and print it in reverse order'''
n = 5873

num = n
lst = []
while num>0:
  last_digit = num%10
  lst.append(last_digit)
  num = num//10
print(lst)