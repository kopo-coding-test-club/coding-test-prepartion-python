def solution(s):
    answer = []
    dict = {}
    
    for i in range(len(s)):
        if(dict.get(s[i]) == None):
            answer.append(-1)
            dict[s[i]] = i
        else:
            answer.append(i - dict.get(s[i]))
            dict[s[i]] = i
    return answer
