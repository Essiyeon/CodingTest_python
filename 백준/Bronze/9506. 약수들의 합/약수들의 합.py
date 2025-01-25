while True:
    arr = []
    n = int(input())
    if n == -1 :
      break;
    
    for i in range(1,n):
      if n%i == 0:
        arr.append(i)

    if sum(arr) == n:
        result = ' + '.join(map(str,arr))
        print(n,'=',result)
    else:
        print(n,'is NOT perfect.')