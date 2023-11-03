import sys; sys.stdin = open("30032.txt", "r")

N, D = map(int, input().split())
for i in range(N):
    word = input()
    ans = ""
    for j in range(len(word)):
        if D == 1:
            if word[j] == "d":
                ans += "q"
            elif word[j] == "b":
                ans += "p"
            elif word[j] == "q":
                ans += "d"
            else:
                ans += "b"
        else:
            if word[j] == "d":
                ans += "b"
            elif word[j] == "b":
                ans += "d"
            elif word[j] == "q":
                ans += "p"
            else:
                ans += "q"
    print(ans)