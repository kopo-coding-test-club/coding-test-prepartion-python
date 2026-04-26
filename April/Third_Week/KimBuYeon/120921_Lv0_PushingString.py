def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if A == B:
            return answer
        else:
            B = B[1 : ] + B[0]
            answer += 1
    else:
        answer = -1        
    return answer