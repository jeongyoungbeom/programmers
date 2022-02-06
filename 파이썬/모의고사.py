def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0, 0, 0]
    for i in range(len(answers)):
        a1 = i % 5
        a2 = i % 8
        a3 = i % 10

        if answers[i] == s1[a1]:
            result[0] += 1
        if answers[i] == s2[a2]:
            result[1] += 1
        if answers[i] == s3[a3]:
            result[2] += 1

    for id, s in enumerate(result):
        if s == max(result):
            answer.append(id + 1)

    return answer