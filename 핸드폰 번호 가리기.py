def solution(phone_number):
    answer = ''
    lens = len(phone_number)
    answer = "*"*(lens-4)
    answer += phone_number[-4:]
    return answer