def solution(my_string, s, e):
    target_str = my_string[s:e+1]
    return my_string[:s] + target_str[::-1] + my_string[e+1:]