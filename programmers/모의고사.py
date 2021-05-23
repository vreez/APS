def solution(answers):
    count = [0] * 3
    for i in range(len(answers)):
        per1 = [0] * len(answers)
        if i % 5 == 0:
            per1[i] = 1
            if per1[i] == answers[i]:
                count[0] += 1
        elif i % 5 == 1:
            per1[i] = 2
            if per1[i] == answers[i]:
                count[0] += 1
        elif i % 5 == 2:
            per1[i] = 3
            if per1[i] == answers[i]:
                count[0] += 1
        elif i % 5 == 3:
            per1[i] = 4
            if per1[i] == answers[i]:
                count[0] += 1
        elif i % 5 == 4:
            per1[i] = 5
            if per1[i] == answers[i]:
                count[0] += 1
    for i in range(len(answers)):
        per2 = [0] * len(answers)
        if i % 2 == 0:
            per2[i] = 2
            if per2[i] == answers[i]:
                count[1] += 1
        elif i % 8 == 1:
            per2[i] = 1
            if per2[i] == answers[i]:
                count[1] += 1
        elif i % 8 == 3:
            per2[i] = 3
            if per2[i] == answers[i]:
                count[1] += 1
        elif i % 8 == 5:
            per2[i] = 4
            if per2[i] == answers[i]:
                count[1] += 1
        elif i % 8 == 7:
            per2[i] = 5
            if per2[i] == answers[i]:
                count[1] += 1
    for i in range(len(answers)):
        per3 = [0] * len(answers)
        if i % 10 < 2:
            per3[i] = 3
            if per3[i] == answers[i]:
                count[2] += 1
        elif 1 < i % 10 < 4:
            per3[i] = 1
            if per3[i] == answers[i]:
                count[2] += 1
        elif 3 < i % 10 < 6:
            per3[i] = 2
            if per3[i] == answers[i]:
                count[2] += 1
        elif 5 < i % 10 < 8:
            per3[i] = 4
            if per3[i] == answers[i]:
                count[2] += 1
        elif 7 < i % 10 < 10:
            per3[i] = 5
            if per3[i] == answers[i]:
                count[2] += 1
    max = count[0]
    for i in range(3):
        if count[i] >= max:
            max = count[i]
    answer = []
    for i in range(3):
        if count[i] == max:
            answer.append(i+1)
    return sorted(answer)