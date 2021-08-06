def solution(citations):
    answer = 0
    arr = sorted(citations, reverse=True)
    for i in range(len(arr), -1, -1):
        if answer != 0:
            break
        else:
            count = 0
            for j in range(len(arr)):
                if arr[j] >= i:
                    count += 1
                else:
                    break
            if count >= i:
                answer = i

    return answer