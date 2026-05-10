def solution(lottos, win_nums):
    match_cnt = 0
    worst_rank = -1
    best_rank = -1 
    for lotto in lottos:
        if lotto in win_nums:
            match_cnt += 1
    zero_cnt = lottos.count(0)
    worst_rank = min(7 - match_cnt, 6)
    best_rank = min(7 - (match_cnt + zero_cnt), 6)
                
    return [best_rank, worst_rank]