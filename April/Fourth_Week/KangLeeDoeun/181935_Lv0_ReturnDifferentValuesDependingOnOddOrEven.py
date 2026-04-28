def solution(n):
    even, odd = 0, 0
    
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            odd = i * i + odd
        return odd
    else:
        for i in range(1, n+1, 2):
            even += i
        return even