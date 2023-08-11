import sys; sys.stdin = open("3062.txt", "r")

N = int(input())
for i in range(N):
    num = input()
    rev = num[::-1]
    total = int(num) + int(rev)
    check = str(total)
    ans = True
    for j in range(len(check)):
        if check[j] == check[len(check)-j-1]:
            ans = True
        else:
            ans = False
            break
    if ans == True:
        print("YES")
    else:
        print("NO")

