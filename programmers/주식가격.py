def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
              if prices[i] > prices[j]:
                break
        times = j - i
        answer.append(times)
    return answer