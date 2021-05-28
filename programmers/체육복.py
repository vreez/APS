def solution(n, lost, reserve):
    answer = 0
    check = [0] * (n + 1)
    # 앞 번호부터 순차적으로 검사하기 위해 정렬을 한다.
    reserve = sorted(reserve)
    for i in range(len(lost)):
        check[lost[i]] = 1
    arr = []
    # 체육복을 잃어버린 사람이 여벌의 체육복을 갖고 있을 경우, 최우선으로 자기 자신이 여벌의 체육복을 가져야 하므로
    # 해당 경우를 미리 확인하고 reserve 배열에서 제외시킨다.
    for i in range(len(reserve)):
        if check[reserve[i]] == 1:
            check[reserve[i]] = 0
        elif check[reserve[i]] == 0:
            arr.append(reserve[i])
    for i in range(len(arr)):
        if arr[i] == 1:
            if check[arr[i]+1] == 1:
                check[arr[i]+1] = 0
        elif arr[i] == n:
            if check[arr[i]-1] == 1:
                check[arr[i]-1] = 0
        else:
            if check[arr[i]-1] == 1:
                check[arr[i]-1] = 0
            elif check[arr[i]+1] == 1:
                check[arr[i]+1] = 0
    for j in range(1, n+1):
        if check[j] == 0:
            answer += 1
    return answer