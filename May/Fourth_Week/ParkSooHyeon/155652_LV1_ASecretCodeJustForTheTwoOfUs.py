def solution(s, skip, index):
    answer = ''
    a = 0
    for i in s:
        r = ord(i)
        while a < index:
            r += 1
            if r > 122:
                r = 97
            while chr(r) in skip:
                r += 1
                if r > 122:
                    r = 97
            a += 1
        a = 0
        answer += chr(r)
    return answer