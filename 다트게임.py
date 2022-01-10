def solution(dartResult):
    answer = []
    n = ""
    for i in dartResult:
        if i.isnumeric():
            n += i
            print(n)
        elif i == 'S':
            n = int(n)**1
            answer.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            answer.append(n)
            n = ''
        elif i == 'T':
            n = int(n)**3
            answer.append(n)
            n = ''
        elif i == '*':
            if len(answer) > 1:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif i == '#' :
            answer[-1] = answer[-1]*-1
    print(answer)
    return sum(answer)
