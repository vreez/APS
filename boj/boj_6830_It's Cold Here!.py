import sys; sys.stdin = open("6830.txt", "r")

check = 201
answer = ""
while True:
    city, temp = input().split()
    if city == "Waterloo":
        temp = int(temp)
        if check >= temp:
            check = temp
            answer = city
        break
    else:
        temp = int(temp)
        if check >= temp:
            check = temp
            answer = city

print(answer)