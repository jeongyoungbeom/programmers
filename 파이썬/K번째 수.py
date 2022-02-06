def solution(array, commands):
    answer = []
    for i in commands:
        q, w, e = i
        new_array = sorted(array[q - 1:w])
        answer.append(new_array[e - 1])

    return answer