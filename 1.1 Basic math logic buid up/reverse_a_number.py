n = 1234

num = n
reversed = 0
while num > 0:
  last_digit = num%10
  reversed=reversed*10+last_digit
  num = num//10
print(reversed)

