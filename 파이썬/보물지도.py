def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        tmp = bin(i | j)[2:]
        if len(tmp) < n :
            tmp = '0'*(n-len(tmp)) + tmp
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', " ")
        answer.append(tmp)
    return answer