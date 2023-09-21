import sys; sys.stdin = open("29863.txt", "r")

night = int(input())
morning = int(input())
if night >= 0 and night <= 3:
    print(morning - night)
else:
    print(24 - night + morning)
