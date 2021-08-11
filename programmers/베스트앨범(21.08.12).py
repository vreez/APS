def solution(genres, plays):
    answer = []
    songs = {}
    for i in range(len(genres)):
        if genres[i] not in songs:
            songs[genres[i]] = plays[i]
        else:
            songs[genres[i]] += plays[i]
    order = sorted(songs.items(), key=lambda x: x[1], reverse=True)

    result = [[] for _ in range(len(order))]
    for i in range(len(order)):
        for j in range(len(genres)):
            if order[i][0] == genres[j]:
                result[i].append([plays[j], j])

    for i in range(len(result)):
        result[i] = sorted(result[i], reverse=True)
        if len(result[i]) > 1:
            for j in range(len(result[i]) - 1):
                if result[i][j][0] == result[i][j + 1][0]:
                    if result[i][j][1] > result[i][j + 1][1]:
                        result[i][j], result[i][j + 1] = result[i][j + 1], result[i][j]
            answer.append(result[i][0][1])
            answer.append(result[i][1][1])
        else:
            answer.append(result[i][0][1])

    return answer