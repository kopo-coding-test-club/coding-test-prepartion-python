def solution(s):
    # 문자가 지금까지 처음 나왔다면 -1
    # 나온적이 있으면 얼마나 앞에서 나왔는지 (본인기준)
    answer = []
    for i in range(len(s)):
        
        # 만약 내 앞에 나온적이 있으면
        if s[i] in s[:i]:
            
            # 내 앞에서 나온 인덱스를 다 모은다음
            idx = list(filter(lambda x: s[x] == s[i], range(i)))
            
            # 가장 근처에 나온 인덱스를 뺀다
            answer.append(i-idx[-1])
        else:
            answer.append(-1)
    return answer
