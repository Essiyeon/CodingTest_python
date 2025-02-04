def solution(keymap, targets):
    answer = []
    key_dict = {}
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            keychar = keymap[i][j]
            if keychar not in key_dict:
                key_dict[keychar] = (j+1)
            else:
                key_dict[keychar] = min(key_dict[keychar],(j+1))
    
    for i in range (len(targets)):
        sum = 0
        for j in range(len(targets[i])):
            if(targets[i][j] in key_dict):
                sum += key_dict[targets[i][j]]
            else:
                sum = -1
                break
        answer.append(sum)

    return answer