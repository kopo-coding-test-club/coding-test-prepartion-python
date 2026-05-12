def solution(answers):
    sp1 = [1, 2, 3, 4, 5]
    sp2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    m = [0, 0, 0]
    
    for i in range(len(answers)):
        if (sp1[i%len(sp1)] == answers[i]): 
            m[0] += 1
        if (sp2[i%len(sp2)] == answers[i]): 
            m[1] += 1
        if (sp3[i%len(sp3)] == answers[i]): 
            m[2] += 1
    
    answer = []

    for idx, value in enumerate(m):
        if value == max(m):
            answer.append(idx+1)
            
    return answer


    
#     sp1_m = len([i for i, j in zip(sp1, answers) if i == j])
#     sp2_m = len([i for i, j in zip(sp2, answers) if i == j])
#     sp3_m = len([i for i, j in zip(sp3, answers) if i == j])
