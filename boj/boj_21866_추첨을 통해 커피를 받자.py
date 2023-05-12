import sys; sys.stdin = open("21866.txt", "r")

score = list(map(int, input().split()))

if sum(score) >= 100:
    if score[0] > 100 or score[1] > 100 or score[2] > 200 or score[3] > 200 or score[4] > 300 or score[5] > 300 or score[6] > 400 or score[7] > 400 or score[8] > 500:
        print("hacker")
    else:
        print("draw")
else:
    print("none")