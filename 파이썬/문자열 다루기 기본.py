def solution(s):
    answer = False
    if (len(s) == 4 or len(s) ==6) and s.isdigit():
        answer = True
    return answer

# isdigit() 숫자로만 이루어져있는지
