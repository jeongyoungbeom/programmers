def solution(N, stages):
    answer = {}
    M = len(stages)
    for i in range(1, N+1):
        if M !=0 :
            answer[i] = stages.count(i)/M
            M -= stages.count(i)
        else:
            answer[i] = 0
    print(sorted(answer, key=lambda i : answer[i], reverse=True))
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))