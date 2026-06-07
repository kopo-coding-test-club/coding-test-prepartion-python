from collections import Counter
def solution(X, Y):
    counter_x = Counter(X)
    counter_y = Counter(Y)
    common_nums_str = list(set(counter_x.keys()) & set(counter_y.keys()))
    common_nums = []
    for common_num_str in common_nums_str:
        min_cnt = min(counter_x[common_num_str], counter_y[common_num_str])
        common_nums += [int(common_num_str)] * min_cnt
    common_nums.sort(reverse=True)
    if not common_nums:
        return "-1"
    answer = "".join(map(str, common_nums))
    if answer[0] == '0':
        return "0"
    return answer