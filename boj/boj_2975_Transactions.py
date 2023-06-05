import sys; sys.stdin = open("2975.txt", "r")

while True:
    ip = list(input().split())
    if ip[0] == '0' and ip[1] == 'W' and ip[2] == '0':
        break
    else:
        if ip[1] == 'W':
            answer = int(ip[0]) - int(ip[2])
        else:
            answer = int(ip[0]) + int(ip[2])
        if answer >= -200:
            print(answer)
        else:
            print("Not allowed")
