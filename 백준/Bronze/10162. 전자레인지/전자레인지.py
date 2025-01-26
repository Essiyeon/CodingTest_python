# A 5분 B 1분 C 10초
A = 300
B = 60
C = 10

T = int(input()) # 초단위

if ((T%A)%B)%C == 0:
  count_a = T//A
  count_b = (T%A)//B
  count_c = ((T%A)%B)//C
  print(count_a,count_b,count_c)
else:
  print(-1)



