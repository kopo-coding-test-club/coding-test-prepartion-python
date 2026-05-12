def solution(lottos, win_nums):
    # 1~45, 6개 번호 복권
    # 일부 번호 안보임 -> 0으로 표기
    # 당첨 가능한 최고 순위, 최저 순위 구하기
    lotto_rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    
    intersect_len = len(list(set(lottos) & set(win_nums)))
    
    unseen_len = lottos.count(0)
    
    high_rank = lotto_rank[intersect_len + unseen_len]
    low_rank = lotto_rank[intersect_len]
    
    answer = [high_rank, low_rank]
    
    return answer