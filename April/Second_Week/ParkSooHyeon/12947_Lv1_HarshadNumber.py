def solution(x):
    result = 0
    a = x
    
    while a > 0:
        n = a%10
        result += n
        a = int(a/10)
    
    answer = True if x%result == 0 else False
    return answer