def solution(begin, target, words):
    answer = 0
    if target not in words:
        answer = 0
    else:
        queue = [begin]
        while queue:
            temp = []
            picked = queue.pop(0)
            if picked == target:
                return answer
            for i in range(len(words)-1, -1, -1):
                count = 0
                for x, y in zip(picked, words[i]):
                    if x != y:
                        count += 1
                if count == 1:
                    temp.append(words.pop(i))
            queue = temp
            answer += 1
    return answer