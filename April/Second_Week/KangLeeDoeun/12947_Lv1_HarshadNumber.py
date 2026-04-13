def solution(x):
    x_sum = 0
    for s in str(x):
        x_sum += int(s)
    
    return True if x % x_sum == 0 else False