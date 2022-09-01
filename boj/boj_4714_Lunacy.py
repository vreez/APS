import sys; sys.stdin = open("4714.txt", "r")

while True:
    num = float(input())
    if num < 0:
        break
    else:
        new = format(num, ".2f")
        answer = format(num * 0.167, ".2f")
        print("Objects weighing {} on Earth will weigh {} on the moon.".format(new, answer))