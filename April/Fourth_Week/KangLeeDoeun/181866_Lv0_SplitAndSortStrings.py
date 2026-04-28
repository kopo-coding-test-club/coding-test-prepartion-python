def solution(myString):
    answer = sorted(myString.split("x"))
    
    result = []
    
    for i in answer:
        if i == '':
            continue
        else:
            result.append(i)
    
    return result