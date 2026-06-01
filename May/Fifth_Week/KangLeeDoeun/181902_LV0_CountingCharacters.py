def solution(my_string):
    answer = [0] * 52
    for s in my_string:
        if s.isupper():
            answer[ord(s)-65] += 1
        elif s.islower():
            answer[ord(s)-71] += 1
    return answer