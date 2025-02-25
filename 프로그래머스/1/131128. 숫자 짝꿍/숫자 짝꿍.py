def solution(X, Y):
    answer = ''
    X_list = list(map(int, str(X)))
    Y_list = list(map(int, str(Y)))
    
    Y_count = {} # Y_list에 각 숫자들(0~9)이 몇 번씩 나오는지 저장
    for y in Y_list:
        Y_count[y] = Y_count.get(y,0)+1 # Y_list.count(y)는 리스트 전체를 순회함
    print(Y_count)
    
    common = []
    
    for x in X_list:
        if Y_count.get(x,0) > 0: # 값이 존재 + 개수가 남아있으면
            common.append(x)
            Y_count[x] -= 1
    
    if len(common) == 0 :
        answer = '-1'
    elif all(c == 0 for c in common):
        answer = '0'
    else:
        common.sort(reverse= True)
        for c in common:
            answer += str(c)
    
    return answer
