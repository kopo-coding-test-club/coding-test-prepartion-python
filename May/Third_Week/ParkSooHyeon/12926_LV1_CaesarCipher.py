def solution(s, n):
    l = list(s)
    answer = ''
    for i in l:
        o = ord(i) + n
        if i.islower() and o > 122:
            answer += (chr(o - 26))
        elif i.isupper() and o > 90:
            answer += (chr(o - 26))
        elif o == 32+n:
            answer += ' '
        else:
            answer += (chr(o))
    return answer