def solution(brown, yellow):
    answer = []
    divisor = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            divisor.append([i, yellow // i])

    for item in divisor:
        if (item[0] + item[1]) * 2 + 4 == brown:
            answer.append(item[0] + 2)
            answer.append(item[1] + 2)

    answer = sorted(answer, reverse=True)
    return answer