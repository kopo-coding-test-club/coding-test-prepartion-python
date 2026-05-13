def solution(d, budget):
    answer = 0
    d.sort()
    sum = 0;
    for m in d:
        sum += m
        answer += 1
        if(sum > budget):
            answer -= 1
            break
    return answer
