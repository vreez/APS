def solution(array, commands):
    answer = []
    for item in commands:
        numbers = array[item[0] - 1:item[1]]
        number = sorted(numbers)[item[2] - 1]
        answer.append(number)
    return answer