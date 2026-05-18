def solution(my_string, queries):
    for query in queries:
        i , j = query
        my_string = my_string[ : i] + my_string[i : j + 1][ : : -1] + my_string[j + 1 : ]
        
    return my_string