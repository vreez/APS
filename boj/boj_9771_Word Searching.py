import sys; sys.stdin = open("9771.txt", "r")
word = input()
ans = 0
try:
    while True:
        sen = input().split()
        for i in sen:
            if word in i:
                ans += 1
except:
    print(ans)