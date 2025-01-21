def solution(n, m, section):
    count = 0
    paint_end = 0

    for start in section:
        if start > paint_end:
            paint_end = start + m -1
            count +=1
    return count