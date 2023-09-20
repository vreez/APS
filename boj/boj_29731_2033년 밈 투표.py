import sys; sys.stdin = open("29731.txt", "r")

li = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
]
ans = True
N = int(input())
for i in range(N):
    sen = input()
    if sen not in li:
        ans = False
        break
if ans == True:
    print("No")
else:
    print("Yes")