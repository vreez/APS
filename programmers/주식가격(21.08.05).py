def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                break
            elif j == len(prices) - 1:
                answer.append(j - i)
            else:
                continue
    answer.append(0)
    return answer