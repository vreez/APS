def solution(progresses, speeds):
    arr = []
    for i in range(len(progresses)):
        if (100 - int(progresses[i])) % int(speeds[i]) == 0:
            arr.append((100 - int(progresses[i])) // int(speeds[i]))
        else:
            arr.append((100 - int(progresses[i])) // int(speeds[i]) + 1)
    num = arr[0]
    answer = []
    count = 1
    for i in range(1, len(arr)):
        if arr[i] <= num:
            if i < len(arr) - 1:
                count += 1
            else:
                count += 1
                answer.append(count)
        else:
            answer.append(count)
            if i < len(arr) - 1:
                count = 1
                num = arr[i]
            else:
                count = 1
                answer.append(count)

    return  answer