def solution(n):
    a = []
    a = list(str(n))
    a.sort(reverse=True)
    return int("".join(a))
