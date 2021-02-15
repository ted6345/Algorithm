def solution(board, moves):
    answer = 0
    stack = []
    top = -1

    for i in moves:
        for j in range(len(board[i - 1])):
            key = board[j][i - 1]
            if key != 0:
                if top != -1:
                    if key == stack[top]:
                        answer += 2
                        stack.pop()
                        top -= 1
                    else:
                        top += 1
                        stack.append(key)
                else:
                    top += 1
                    stack.append(key)
                board[j][i - 1] = 0

                break

    return answer