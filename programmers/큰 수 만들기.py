def solution(number, k):
    answer = ''
    # 문자열에 담겨 있는 수를 리스트에 하나씩 쪼개서 담는다.
    number = list(number)
    # number의 가장 앞에 있는 수를 result에 담는다.
    result = [number[0]]
    # count는 제거해야 할 숫자의 개수이다.
    count = k
    # for문을 활용해 number안의 수를 하나씩 확인한다. 이때, count가 0보다 크고 result가 빈 배열이 아니며,
    # result의 맨 뒤에 위치한 숫자가 확인해야 할 number의 숫자보다 작을 경우,
    # (이 조건이 성립할 때까지 while문을 사용해 숫자를 빼고 카운트를 줄이는 과정을 반복한다.)
    # result의 맨 뒤의 값을 삭제한다. 이 때는 수를 제거했다는 의미로 count를 하나 줄인다.
    # 위의 조건이 성립하지 않으면 result의 마지막 수보다 더 큰 수인 number의 숫자를 result에 넣는다.
    for i in range(1, len(number)):
        while count > 0 and len(result) > 0 and int(result[-1]) < int(number[i]):
            result.pop()
            count -= 1
        result.append(number[i])
    # number안의 모든 숫자를 확인한 뒤에도 count가 0보다 클 경우, result의 뒤에서부터 count만큼의 숫자를 잘라낸다.
    if count > 0:
        result = result[:len(result) - count]
    # 리스트 형식인 result를 문자열로 변형한다.
    answer = ''.join(result)
    return answer