import string
def solution(s, skip, index):
    lower_alphabets = list(string.ascii_lowercase)
    filtered_lower_alphabets = list(filter(lambda x : x not in skip, lower_alphabets))
    answer = ''
    for i in range(len(s)):
        c_idx = filtered_lower_alphabets.index(s[i])
        answer += filtered_lower_alphabets[(c_idx + index) % len(filtered_lower_alphabets)]
    return answer