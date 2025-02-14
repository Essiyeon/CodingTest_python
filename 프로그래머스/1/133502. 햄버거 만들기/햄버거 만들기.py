def solution(ingredient):
    burger = []
    count = 0
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1,2,3,1]:
            count += 1
            for _ in range(4):
                burger.pop()
    return count