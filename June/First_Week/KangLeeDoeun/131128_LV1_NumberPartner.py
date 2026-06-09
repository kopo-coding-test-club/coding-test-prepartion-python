from collections import Counter
def solution(X, Y):
    common_counts = Counter(X) & Counter(Y)

    if not common_counts:
        return "-1"
        
    answer = []
    
    # 큰 수부터
    for i in range(9, -1, -1):
        num_str = str(i)
        # 개수만큼 곱해서 정답에 추가
        if common_counts[num_str] > 0:
            answer.append(num_str * common_counts[num_str])
            
    result = "".join(answer)
    
    #  0으로만 시작하는 경우 "0" 반환
    if result[0] == '0':
        return "0"
        
    return result
    