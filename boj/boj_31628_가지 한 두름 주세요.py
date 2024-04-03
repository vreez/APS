import sys; sys.stdin = open("31628.txt", "r")

flag = False
arr = [list(input().split()) for _ in range(10)]
new = []
for i in range(10):
    if len(set(arr[i])) == 1:
        flag = True
if flag == False:
    for i in range(10):
        nums = []
        for j in range(10):
            nums.append(arr[j][i])
        if len(set(nums)) == 1:
            flag = True

if flag == True:
    print(1)
else:
    print(0)



