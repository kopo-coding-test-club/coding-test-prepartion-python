def solution(my_string, queries):
    # queries의 원소는 [s, e]
    # my_string의 인덱스 s~e까지 뒤집어라
    
    for query in queries:
        s, e = query[0], query[1]+1

        my_string = my_string[:s] + my_string[s:e][::-1] + my_string[e:]

    return my_string