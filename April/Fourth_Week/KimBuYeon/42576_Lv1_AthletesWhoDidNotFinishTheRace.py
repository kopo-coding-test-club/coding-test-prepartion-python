from collections import defaultdict
def solution(participant, completion):
    participant_dict = defaultdict(int)
    for p in participant:
        participant_dict[p] += 1
    
    for c in completion:
        if c in participant_dict:
            participant_dict[c] -= 1
    
    return [k for k in participant_dict if participant_dict[k] !=0][0]
    