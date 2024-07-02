import sys; sys.stdin = open("3943.txt", "r")

T = int(input())
for i in range(T):
    num = int(input())
    arr = []
    while True:
        arr.append(num)
        if num == 1:
            break
        else:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num * 3 + 1
    print(max(arr))
