def solution(d, budget):
    answer = 0
    total_sum = 0
    d.sort()
    for i in range(len(d)):
        total_sum += d[i]
        if total_sum > budget:
            break
        else:
            answer += 1
    return answer