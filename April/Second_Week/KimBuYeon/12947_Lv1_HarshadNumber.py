def solution(x):
    answer = False
    r_num = x
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    if r_num % int(s) == 0:
        answer = True
        
    return answer