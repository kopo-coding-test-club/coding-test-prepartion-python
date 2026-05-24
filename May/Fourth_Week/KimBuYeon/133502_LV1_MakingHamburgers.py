def solution(ingredient):
    answer = 0
    ingredients = []    
    for i in range(len(ingredient)):
        ingredients.append(ingredient[i])
        if ingredients[-4 : ] == [1, 2 , 3, 1]:
            del ingredients[-4 : ]
            answer += 1
    
    return answer