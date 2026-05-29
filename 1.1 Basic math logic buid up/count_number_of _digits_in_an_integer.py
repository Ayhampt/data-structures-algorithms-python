n = 5873

num = n
count = 0
while num > 0:
  count+=1
  num = num//10
print(count)


'''Time complexity ->  O(log10(N)) How? -> the number of iteration depends
on the value 10 number of times while loop is based of the num//10
so o(log10(N))'''