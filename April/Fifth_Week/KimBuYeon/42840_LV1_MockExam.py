def solution(answers):
    answer = []
    
    answer_sheets = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    c_dict = {
        1 : 0,
        2 : 0, 
        3 : 0
    }
    
    #이차원 리스트의 인덱스에 들어갈 값의 위치를 바꾸는 생각 필요
    for i in range(len(answers)):
        for j in range(len(answer_sheets)):
            if answers[i] == answer_sheets[j][i % len(answer_sheets[j])]:
                c_dict[j + 1] += 1
    answer = sorted([k for k , v in c_dict.items() if max(c_dict.values()) == v])
    
    return answer