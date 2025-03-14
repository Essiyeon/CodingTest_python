n, m = map(int, input().split())

numbers = list(map(int, input().split()))

max_sum = 0
for i in range(n - 2):  
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            current_sum = numbers[i] + numbers[j] + numbers[k]
            if current_sum <= m:
                max_sum = max(max_sum, current_sum)
print(max_sum)
  