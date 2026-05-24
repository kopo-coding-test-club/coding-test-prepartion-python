def solution(s):
    int_s = sorted(list(map(int, s.split(" "))))
    str_s = str(int_s[0]) + " " + str(int_s[-1])
    return str_s