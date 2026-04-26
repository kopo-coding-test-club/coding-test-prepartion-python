def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced_array = array[i - 1 : j]
        e = sorted(sliced_array)[k-1]
        answer.append(e)
    return answer