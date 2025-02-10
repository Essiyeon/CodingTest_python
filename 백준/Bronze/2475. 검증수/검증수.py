arr = input().split()

for i in range(len(arr)):
  arr[i] = int(arr[i])
  arr[i] = arr[i]*arr[i]

unique = sum(arr)%10
print(unique)
