def solution(board, moves):
    answer = 0
    machine = []
    pick = []
    for _ in range(len(board)):
        machine.append([])
        
    for i in reversed(board):
        for j in range(len(board)):
            if i[j] != 0:
                machine[j].append(i[j])
    print(machine)
    for i in moves:
        if machine[i - 1]: 
            num = machine[i - 1].pop()
       
            if len(pick) != 0:
                if pick[-1] == num:
                    answer += 2
                    pick.pop()
                else:
                    pick.append(num)
            else:
                pick.append(num)
    return answer
