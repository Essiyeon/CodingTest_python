n, k = map(int, input().split())
m = n - k

n_fact = 1
k_fact = 1
m_fact = 1

for i in range(1,n+1):
  n_fact *= i
for i in range(1,k+1):
  k_fact *= i
for i in range(1,m+1):
  m_fact *= i

result = n_fact//(m_fact*k_fact)
print(result)