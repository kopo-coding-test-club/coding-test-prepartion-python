def solution(my_string, overwrite_string, s):
    old_len = len(overwrite_string)
    replace_string = my_string.replace(my_string[s:], overwrite_string, 1)
    return replace_string + my_string[s+old_len:]