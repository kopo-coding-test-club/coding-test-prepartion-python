# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
def solution(myString, pat):
    answer = myString[:myString.rfind(pat)+len(pat)]
    return answer