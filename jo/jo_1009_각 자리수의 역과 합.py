import  sys; sys.stdin = open("1009.txt", "r")

while True:
    num = int(input())
    if num == 0:
        break
    else:
        new = str(num)[::-1]
        check = list(map(int, new))
        total = sum(check)
        print(int(new), total)
