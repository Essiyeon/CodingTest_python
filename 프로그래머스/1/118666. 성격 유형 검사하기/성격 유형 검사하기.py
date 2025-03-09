def solution(survey, choices):
    answer = ''
    kind = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    # 1번 지표	라이언형(R), 튜브형(T)
    # 2번 지표	콘형(C), 프로도형(F)
    # 3번 지표	제이지형(J), 무지형(M)
    # 4번 지표	어피치형(A), 네오형(N)
    
    for i in range(len(survey)):
        front, back = survey[i][0], survey[i][1]
        choice = choices[i]
        
        if choice < 4 :
            kind[front] += 4 - choice
        elif choice > 4 :
            kind[back] += choice - 4
    
    answer += 'R' if kind['R'] >= kind['T'] else 'T'
    answer += 'C' if kind['C'] >= kind['F'] else 'F'
    answer += 'J' if kind['J'] >= kind['M'] else 'M'
    answer += 'A' if kind['A'] >= kind['N'] else 'N'
    
    
    return answer