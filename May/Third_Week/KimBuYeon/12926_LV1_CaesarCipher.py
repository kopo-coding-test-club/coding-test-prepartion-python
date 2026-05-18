import string
def solution(s, n):
    answer = ''
    l_alphabet = list(string.ascii_lowercase)
    u_alphabet = list(string.ascii_uppercase)
    idx = 0
    for i in range(len(s)):
        if s[i] in l_alphabet:
            idx = l_alphabet.index(s[i])
            answer += l_alphabet[(idx + n) % len(l_alphabet)]
        elif s[i] in u_alphabet:
            idx = u_alphabet.index(s[i])
            answer += u_alphabet[(idx + n) % len(u_alphabet)]
        elif s[i] == " ":
            answer += " "
    return answer