def solution(clothes):
    arr = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in arr:
            arr[clothes[i][1]] = 1
        else:
            arr[clothes[i][1]] += 1
    total = 1
    for value in arr.values():
        total *= (value + 1)
    answer = total - 1
    return answer