def solution(lottos, win_nums):
    answer = []
    grade = [6, 5, 4, 3, 2]
    first = 0;
    last = 0;

    for win in win_nums:
        for lotto in lottos:
            if(win == lotto):
                first += 1;
                last += 1;

    
    for lotto in lottos:
        if(lotto == 0):
            first += 1;
    
    if(first <= 1):
        answer.append(6)
    else:
        answer.append(grade.index(first) + 1)
    if(last <= 1):
        answer.append(6)
    else:
        answer.append(grade.index(last) + 1)
    
    
    
    
    return answer
