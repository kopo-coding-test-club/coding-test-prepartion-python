def solution(s):
    answer = ''
    list = s.split(" ")
    nums = []
    for n in list:
        nums.append(int(n))
        
    answer += str(min(nums)) + " " + str(max(nums))
    return answer
