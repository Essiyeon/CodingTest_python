n = int(input())
pack = 1

for i in range(n,1,-1):
  pack *= i

string_pack = str(pack)
string_pack = string_pack[::-1]
# print(string_pack)

count = 0

for i in range(len(string_pack)):
  if string_pack[0] == '0':
    if string_pack[i] =='0':
      count += 1
    else:
      break
  else:
    break
print(count)
    
    
