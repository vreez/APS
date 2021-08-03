def solution(priorities, location):
    answer = 0
    printer = [[0, 0] for _ in range(len(priorities))]
    result = []
    # printer 배열에 중요도와 초기 index를 저장한다.
    for i in range(len(priorities)):
        printer[i][0] = priorities[i]
        printer[i][1] = i
    # printer에 문서가 아무것도 남지 않을 때까지 확인과정을 반복한다.
    while printer:
        # printer 목록 가운데 가장 앞에 있는 문서의 중요도가 다른 어떤 문서보다 가장 중요하면 출력이 가능하므로
        # 출력목록을 의미하는 result에 가장 앞에 위치한 문서를 더해준다.
        if printer[0][0] >= max(printer)[0]:
            result.append(printer.pop(0))
        # 그렇지 않으면 printer 목록 가운데 가장 앞에 위치한 문서를 맨 뒤로 보낸다.
        else:
            printer.append(printer.pop(0))
    # 출력을 모두 마친 후, 출력 목록인 result를 하나씩 확인하며 location에 해당하는 문서의 출력순서(result에 저장된 index)를 출력해준다.
    for i in range(len(result)):
        if result[i][1] == location:
            answer = i + 1
    return answer