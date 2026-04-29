from collections import Counter

def solution(participant, completion):
    
    remove = Counter(completion)
    
    for i in participant:
        if remove[i] > 0:
            remove[i] -= 1
        else:
            result = i
    
    return result