def solution(board, moves):
    stack = []
    count = 0
    
    for col in moves:
        row = 0
        col -= 1
        while row < len(board): 

            # 인형이 없는 곳에서 크레인 작동시
            if board[len(board)-1][col] == 0:
                break
                
            # 0이면 다음 행 순회
            if board[row][col] == 0:
                row += 1
                continue
                
            # stack 이전 값이랑 뽑는 값이랑 같으면
            if len(stack) > 0 and stack[-1] == board[row][col]:
                count += 1
                stack.pop()

                # 집었으니 0으로 표현
                board[row][col] = 0
                break
            else:
                # 안 같으면 stack에 추가
                stack.append(board[row][col])

                # 집었으니 0으로 표현
                board[row][col] = 0
                break

    return count * 2
