def solution(ingredient):
    stack = []
    count = 0
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            count += 1
            del stack[-4:]
            
    return count