def solution(scores):
    answer = ''
    result = []
    for i in range(len(scores)):
        items = []
        for j in range(len(scores)):
            items.append(scores[j][i])
        if items.count(items[i]) <= 1:
            if items[i] == max(items) or items[i] == min(items):
                items.pop(i)
        average = (sum(items) / len(items))

        if average >= 90:
            answer += 'A'
        elif average >= 80:
            answer += 'B'
        elif average >= 70:
            answer += 'C'
        elif average >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer