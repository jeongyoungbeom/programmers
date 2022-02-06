def solution(nums):
    answer = 0
    length = len(nums)//2
    new_nums = list(set(nums))
    if length > len(new_nums):
        answer = len(new_nums)
    else:
        answer = length
    return answer