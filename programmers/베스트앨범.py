def solution(genres, plays):
    answer = []
    count = {}
    for i in range(len(genres)):
        if genres[i] not in count:
            count[genres[i]] = plays[i]
        else:
            count[genres[i]] += plays[i]
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)
    sorted_genres = [0] * len(result)
    for i in range(len(result)):
        sorted_genres[i] = result[i][0]
    music = []
    for pair in zip(genres, plays):
        music.append(pair)
    sorted_plays = [[] for _ in range(len(sorted_genres))]
    for i in range(len(music)):
        for j in range(len(sorted_genres)):
            if music[i][0] == sorted_genres[j]:
                sorted_plays[j].append([music[i][1], i])
    for i in range(len(sorted_plays)):
        arr = sorted(sorted_plays[i], reverse = True)
        for a in range(len(arr)-1):
            n = 0
            m = 0
            if a < len(arr)-1:
                if arr[a][0] == arr[a+1][0] and arr[a][1] > arr[a+1][1] :
                    n = arr[a][1]
                    m = arr[a+1][1]
                    arr[a][1] = m
                    arr[a+1][1] = n
        if len(arr) >= 2:
            for j in range(2):
                answer.append(arr[j][1])
        else:
            answer.append(arr[0][1])
    return answer