import string
def solution(my_string):
    alpha = list(set(",".join(my_string).split(",")))
    alphabets = list(string.ascii_uppercase + string.ascii_lowercase)
    cnts = [0] * len(alphabets)
    for i in range(len(alpha)):
        idx = alphabets.index(alpha[i])
        cnt = my_string.count(alpha[i])
        cnts[idx] = cnt
    return cnts