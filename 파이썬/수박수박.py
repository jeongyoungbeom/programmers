# def solution(n):
#     answer = ''
#     answer = "수박" * n
#     return answer[:n]

def solution(n):
    answer = ''
    for i in range(n):
        if i%2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer