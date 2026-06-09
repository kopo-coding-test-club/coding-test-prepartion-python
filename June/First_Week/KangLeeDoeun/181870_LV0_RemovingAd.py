def solution(strArr):
    # answer = []
    # for s in strArr:
    #     if "ad" in s:
    #         continue
    #     else:
    #         answer.append(s)
    # return answer
    return [a for a in strArr if "ad" not in a]