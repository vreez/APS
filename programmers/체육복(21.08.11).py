def solution(n, lost, reserve):
    answer = 0
    students = []
    for i in range(1, n + 1):
        students.append(i)

    lost = sorted(lost)
    reserve = sorted(reserve)
    # 여벌 체육복을 가지고 있는 사람이 체육복을 잃어버렸을 경우를 가장 먼저 확인한다.
    complete = []
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            complete.append(lost[i])
    # 여벌 체육복을 가지고 있지 않은 경우, 자신의 앞번호 사람이 여벌 체육복을 가지고 있는지
    # 먼저 확인하고, 없을 경우 뒷번호 사람이 여벌 체육복이 있는지 확인한다.
    # 앞뒤 사람 모두 여벌 체육복을 가지고 있지 않을 경우, 체육복을 빌릴 수 없다.
    for i in range(len(lost)):
        if lost[i] not in complete:
            if lost[i] - 1 in reserve:
                reserve.remove(lost[i] - 1)
            elif lost[i] + 1 in reserve:
                reserve.remove(lost[i] + 1)
            else:
                n -= 1
    answer = n
    return answer