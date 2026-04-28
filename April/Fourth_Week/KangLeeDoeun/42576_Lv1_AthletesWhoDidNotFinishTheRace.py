def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
        
    return participant[-1]
    # for i in participant:
    #     if i not in completion:
    #         return i
    #     else:
    #         completion.remove(i)