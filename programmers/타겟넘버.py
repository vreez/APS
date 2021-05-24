def solution(numbers, target):
    answer = 0
    arr = [0]
    # numbers에 담긴 숫자갯수 만큼 for문을 돌며 +와 - 계산을 반복한다.
    for i in range(len(numbers)):
        # 계산한 결과를 담을 result 배열을 생성한다.
        result = []
        # 기존의 계산된 결과에 numbers에 담긴 숫자를 하나씩 더하고 뺀 값을 추가한다.
        for num in arr:
            result.append(num + numbers[i])
            result.append(num - numbers[i])
        # arr 배열에 새롭게 계산된 결과를 담는다.
        arr = result
    # 마지막 인덱스까지 모두 계산한 최종 값이 target과 같은 값이 나오면 answer을 1씩 더한다.
    for i in range(len(arr)):
        if arr[i] == target:
            answer += 1
    return answer

# print(solution([1,1,1,1,1], 3))