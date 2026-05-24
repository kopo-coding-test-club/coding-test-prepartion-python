import string
def solution(s, skip, index):
    list_alphabet = [x for x in list(string.ascii_lowercase) if x not in skip]
    answer = ''
    
    for i in s:
        answer += list_alphabet[(list_alphabet.index(i) + index) % len(list_alphabet)]
    
    return answer