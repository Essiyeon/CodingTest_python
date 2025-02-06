def solution(keymap, targets):
    answer = []
    dict = {}

    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] in dict :
                dict[keymap[i][j]] = min(dict[keymap[i][j]], j+1)
            else:
                dict[keymap[i][j]] = j+1

    for i in range(len(targets)):
        sum = 0
        for j in range(len(targets[i])):
            if targets[i][j] in dict:
                sum += dict[targets[i][j]]
            else:
                sum = -1
                break
        answer.append(sum)
    return answer