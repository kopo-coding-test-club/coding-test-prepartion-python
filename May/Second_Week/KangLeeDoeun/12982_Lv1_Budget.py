def solution(d, budget):
    # 최대한 많은 부서의 물품 구매
    # d는 부서별로 신청 금액이 들어있는 배열
    # 부서별 신청 금액은 1이상 100000이하
    # budget은 예산
    total = 0
    answer = 0
    for i in sorted(d):
        if total + i > budget:
            break
        total += i
        answer += 1
    return answer