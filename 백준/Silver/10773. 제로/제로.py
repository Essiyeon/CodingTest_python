K = int(input())
nums = []
for _ in range(K):
  n = int(input())
  if n != 0:
    nums.append(n)
  else:
    nums.pop()
print(sum(nums))