def solution(array, commands):
    answer = []
    for command in commands:
        sort_array = sorted(array[command[0]-1:command[1]])
        answer.append(sort_array[command[2]-1])
    return answer