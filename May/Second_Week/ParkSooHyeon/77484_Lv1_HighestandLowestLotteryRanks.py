def solution(lottos, win_nums):
    answer = [0, 0]
    max_r, min_r = 0, 0
    
    for i in lottos:
        if i in win_nums:
            max_r += 1
            min_r += 1
        elif i == 0:
            max_r += 1
    
    if (7-max_r) > 5:
        answer[0] = 6
    else:
        answer[0] = 7-max_r
    if (7-min_r) > 5:
        answer[1] = 6
    else:
        answer[1] = 7-min_r
    
    return answer