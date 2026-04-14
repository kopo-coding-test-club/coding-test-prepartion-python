def solution(myString, pat):
    last = -1
    for i in range(len(myString)):
        if myString[i : i + len(pat)] == pat:
            last = i
    
    return myString[:last + len(pat)]