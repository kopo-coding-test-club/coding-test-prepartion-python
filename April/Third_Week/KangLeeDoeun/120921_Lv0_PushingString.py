def solution(A, B):
    count = 1
    len_A = len(A) 
    
    if A == B:
        return 0
    
    for i in range(0, len_A):
        sub_str = A[len_A-i-1::]
        plus_str = sub_str + A[:len_A-i-1]
        
        if plus_str == B:            
            return count    
        count += 1
        
    return -1