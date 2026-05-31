from collections import defaultdict
def solution(board, moves):
    dolls_dict = defaultdict(list)
    answer = 0
    stack = []
    t_board = list(zip(*board))
    for i in range(len(t_board)):
        f_board = list(filter(lambda x : x != 0 , t_board[i]))
        dolls_dict[i + 1] = f_board
    for move in moves:
        if len(dolls_dict[move]) > 0:
           stack.append(dolls_dict[move][0])
           dolls_dict[move].pop(0)
        if len(stack) >=2 and stack[-1] == stack[-2]:
            del stack[-2 : ]
            answer += 2
    
    return answer