import sys; sys.stdin = open("1516.txt", "r")

while True:
    words = []
    count = 0
    N = input()
    if N == "END":
        break
    else:
        words.append(N.split(" "))
        count += 1

    answer = {}
    for i in range(count):
        for j in range(len(words[i])):
            if words[i][j] not in answer:
                answer[words[i][j]] = 1
            else:
                answer[words[i][j]] += 1
    sorted_answer = sorted(answer.items(), key = lambda x:x[0])
    for key, value in sorted_answer:
        print("{} : {}".format(key, value))

