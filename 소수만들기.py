from itertools import combinations
def is_prime_number(num):
    if num == 1 or num == 0:
        return False
    else:
        for i in range(2, (num//2)+1):
            if num%i == 0:
                return False
        return True

def solution(nums):
    answer = 0
    cmb = list(combinations(nums, 3))
    for i in cmb:
        if is_prime_number(sum(i)):
            answer += 1
    return answer

print(solution([1, 2, 3, 7, 6, 4]))