def solution(s):
    answer = False
    alphabets = s.lower()
    p_cnt = alphabets.count("p")
    y_cnt = alphabets.count("y")
    if p_cnt == y_cnt:
        answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer