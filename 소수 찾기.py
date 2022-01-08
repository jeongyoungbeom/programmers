def solution(n):
    answer = 0
    list = [True] * (n+1)
    a = int(n**0.5)
    for i in range(2, a+1):
        if list[i] == True:
            for j in range(i+i, n+1, i):
                list[j] = False
    for i in range(2, n+1):
        if list[i] == True:
            answer += 1
    return answer


# def solution(n):
#     list = set(range(2, n + 1))
# 
#     for i in range(2, n + 1):
#         if i in list:
#             list -= set(range(i + i, n + 1, i))
#     return len(list)