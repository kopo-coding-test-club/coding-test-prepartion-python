def solution(s, skip, index):
    answer = ''
    
    for i in s:
        count = 1
        str = i
        while count <= index:
            str = ord(str) + 1
            if str > 122:
                str = 97
            str = chr(str)
            if str not in skip: count += 1
        answer += str
    return answer
