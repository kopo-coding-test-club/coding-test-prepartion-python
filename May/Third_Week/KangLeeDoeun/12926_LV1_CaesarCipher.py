def solution(s, n):
    # 파이썬에서는 ord()와 chr() 함수를 통해 문자를 아스키코드로, 아스키코드를 문자로 변환할 수 있다.
    answer=''
    for i in s:

        if i == ' ':
            answer += ' '
            
        if i.islower():
            if ord(i) + n > 122:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
            
        if i.isupper():
            if ord(i) + n > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
    return answer