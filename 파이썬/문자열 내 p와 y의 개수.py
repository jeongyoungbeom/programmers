def solution(s):
    answer = True
    s = s.upper()
    a = []
    if s.count('P') != s.count('Y'):
        answer = False
    return answer