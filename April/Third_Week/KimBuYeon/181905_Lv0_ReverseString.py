def solution(my_string, s, e):
    answer = ""
    part_of_string = my_string[s : e + 1]
    reversed_string = part_of_string[ : : -1] 
    answer = my_string[ : s] + reversed_string + my_string[e+1 : ]
    return answer