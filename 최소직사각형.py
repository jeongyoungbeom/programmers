def solution(sizes):
    answer = 0
    sizes = [sorted(i, reverse=True) for i in sizes]
    widths = [size[0] for size in sizes]
    heights = [size[1] for size in sizes]
    answer = max(widths) * max(heights)
    return answer


n = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(n))



# def solution(sizes):
#     answer = 0
#     w_size = []
#     h_size = []
#     for i in range(len(sizes)):
#         if sizes[i][0] > sizes[i][1]:
#             w_size.append(sizes[i][0])
#             h_size.append(sizes[i][1])
#         else:
#             h_size.append(sizes[i][0])
#             w_size.append(sizes[i][1])
#     answer = max(h_size) * max(w_size)
#     return answer