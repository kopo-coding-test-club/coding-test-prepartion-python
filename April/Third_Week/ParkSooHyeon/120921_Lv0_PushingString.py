def solution(A, B):
    if(A == B):
        return 0
    
    result = A[len(A)-1]+A[0:len(A)-1]
        
    for i in range(len(A)+1):
        if (result == B):
            return i+1
        else:
            answer = -1
            result = result[len(A)-1]+result[0:len(A)-1] 
    return answer