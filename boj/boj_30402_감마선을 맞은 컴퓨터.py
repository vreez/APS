import sys; sys.stdin = open("30402.txt", "r")

arr = [list(input().split()) for _ in range(15)]
ans = ""
for i in range(15):
    if 'w' in arr[i]:
        ans = "w"
    elif "b" in arr[i]:
        ans = "b"
    elif "g" in arr[i]:
        ans = "g"
if ans == "w":
    print("chunbae")
elif ans == "b":
    print("nabi")
else:
    print("yeongcheol")

