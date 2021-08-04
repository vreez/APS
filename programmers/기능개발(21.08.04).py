def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            days.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            days.append((100 - progresses[i]) // speeds[i])
    count = 1
    maxNum = days[0]
    for i in range(1, len(days)):
        if days[i] > maxNum:
            answer.append(count)
            maxNum = days[i]
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer