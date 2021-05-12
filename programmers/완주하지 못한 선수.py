def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(participant)):
        if i < len(participant)-1:
            if participant[i] != completion[i]:
                answer = participant[i]
                break
        else:
            answer = participant[i]

    return answer