import sys; sys.stdin = open("4758.txt", "r")

while True:
    speed, weight, strength = map(float, input().split())
    check = False
    if speed == weight and weight == strength and speed == 0:
        break
    else:
        if speed <= 4.5 and weight >= 150 and strength >= 200:
            print("Wide Receiver", end=" ")
            check = True
        if speed <= 6.0 and weight >= 300 and strength >= 500:
            print("Lineman", end=" ")
            check = True
        if speed <= 5.0 and weight >= 200 and strength >= 300:
            print("Quarterback", end=" ")
            check = True
        if check == False:
            print("No positions", end="")
    print()