c= 'azihaazihkla'
q = ['a','z','i','l']
hash_map = [0]*26
result = []

for char in c:
  ascii = ord(char)
  #print(ascii)
  index = ascii - 97
  hash_map[index] +=1
for el in q:
  index = ord(el)-97
  re = hash_map[index]
  result.append(re)
print(result)
