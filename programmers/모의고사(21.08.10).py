def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = []
    result = []
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(answers)):
        if answers[i] == person1[i % len(person1)]:
            count1 += 1
        if answers[i] == person2[i % len(person2)]:
            count2 += 1
        if answers[i] == person3[i % len(person3)]:
            count3 += 1

    result.append(count1)
    result.append(count2)
    result.append(count3)
    maxCount = max(result)
    for i in range(3):
        if result[i] == maxCount:
            answer.append(i + 1)

    return answer