def solution(d, budget):
    answer = 0
    total = 0
    m = 0
    d.sort()
    
    for i in range(0, len(d)):
        total += d[i]
        if total <= budget:
            answer = i+1
            
    return answer