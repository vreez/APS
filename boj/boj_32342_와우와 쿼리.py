import sys; sys.stdin = open("32342.txt", "r")

Q = int(input())
for i in range(Q):
    word = input()
    ans = 0
    for j in range(len(word)-2):
        if word[j:j+3] == "WOW":
            ans += 1
    print(ans)