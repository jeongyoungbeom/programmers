def solution(n):
    answer = 0
    a = n ** 0.5
    if a == int(a):
        answer = (a + 1) ** 2
    else:
        answer = -1

    return int(answer)