def solution(s):
    strings = s.split(" ")
    c_str_list = [string.capitalize() for string in strings]
    return " ".join(c_str_list)