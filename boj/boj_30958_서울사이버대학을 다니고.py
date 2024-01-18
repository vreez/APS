import sys; sys.stdin = open("30958.txt", "r")

N = int(input())
ans = {
    'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0,
    'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0,
    'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0,
    'y':0, 'z':0
}
arr = list(input().split())
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "," or arr[i][j] == ".":
            continue
        else:
            ans[arr[i][j]] += 1
print(max(ans.values()))