def solution(numbers, target):
    answer = 0
    queue = [0]
    for number in numbers:
        result = []
        for item in queue:
            result.append(item + number)
            result.append(item - number)
        queue = result

    for i in range(len(queue)):
        if queue[i] == target:
            answer += 1

    return answer