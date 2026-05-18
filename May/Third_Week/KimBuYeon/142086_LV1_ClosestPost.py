def solution(s):
    answer = []
    location_dict = {}
    for i in range(len(s)): 
        if s[i] not in location_dict:
            answer.append(-1)
        else:     
            answer.append(i - location_dict[s[i]])
        location_dict[s[i]] = i
    return answer