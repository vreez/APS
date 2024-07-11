import sys; sys.stdin = open("4287.txt", "r")

while True:
    words = list(input().split())
    if words[0] == "#":
        break
    else:
        num = []
        last = ""
        for i in range(len(words[0])):
            ans = ord(words[1][i]) - ord(words[0][i])
            num.append(ans)
        for j in range(len(num)):
            res = ord(words[2][j]) + num[j]
            if res > 122:
                res -= 26
            if res < 97:
                res += 26
            last += chr(res)
        print(words[0], words[1], words[2], last)
