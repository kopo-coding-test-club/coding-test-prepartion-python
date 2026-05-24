def solution(s):
    answer = ''
    nums = list(map(int , s.split(" ")))
    min_num_str = str(min(nums))
    max_num_str = str(max(nums))
    answer = " ".join([min_num_str, max_num_str])
    return answer