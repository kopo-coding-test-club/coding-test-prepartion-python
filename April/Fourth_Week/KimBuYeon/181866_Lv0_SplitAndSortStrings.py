def solution(myString):
    answer = []
    splited_string = list(filter(None, myString.split("x")))
    answer = sorted(splited_string, key=str.lower)
    return answer