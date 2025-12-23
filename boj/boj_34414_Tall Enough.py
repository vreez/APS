n = int(input())
check = "True"
for i in range(n):
    if int(input()) < 48:
        check = "False"
        break
print(check)