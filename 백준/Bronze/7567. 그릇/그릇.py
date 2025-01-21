plat = input()
height = 0

for i in range(0,len(plat)-1):
  if plat[i] == plat[i+1]:
    height += 5
  else:
    height += 10

print(height+10)



