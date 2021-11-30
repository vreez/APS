import sys; sys.stdin = open("2083.txt", "r")

while True:
    name, age, weight = input().split()
    if name == '#':
        break
    else:
        if int(age) > 17 or int(weight) >= 80:
            print(name + " Senior")
        else:
            print(name + " Junior")