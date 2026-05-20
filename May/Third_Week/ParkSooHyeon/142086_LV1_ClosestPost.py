def solution(s):
    answer = []
    for i in range(0, len(s)):
        f = s.find(s[i], 0, i)
        if f > -1:
            c = s.rfind(s[i], 0, i)
            answer.append(i-c)
        else:
            answer.append(f)
    return answer