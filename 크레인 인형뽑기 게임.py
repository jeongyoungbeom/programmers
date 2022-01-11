def solution(board, moves):
    answer = 0
    list = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                list.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(list) > 1:
                    if list[-1] == list[-2]:
                        list.pop(-1)
                        list.pop(-1)
                        answer += 2
                break
    return answer