def solution(food):
    answer = ''
    f_num = 1
    for i in range(1, len(food)):
        answer += str(f_num) * (food[i] // 2)
        f_num += 1
    answer += "0"
    f_num = len(food) - 1
    for i in range(len(food) - 1, 0, -1):
        answer += str(f_num) * (food[i] // 2)
        f_num -= 1
    
    return answer