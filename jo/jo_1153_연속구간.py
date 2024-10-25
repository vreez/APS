import sys; sys.stdin = open("1153.txt", "r")

for _ in range(3):
    num = int(input())
    new = str(num)
    check = 1
    ans = []
    if len(new) > 1:
        for i in range(len(new)-1):
            if new[i] == new[i+1]:
                check += 1
            else:
                ans.append(check)
                check = 1
        ans.append(check)
    else:
        ans.append(1)
    print(max(ans))

