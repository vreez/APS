import sys; sys.stdin = open("826.txt", "r")

while True:
    print("1. Korea")
    print("2. USA")
    print("3. Japan")
    print("4. China")
    print("number?", end=" ")
    N = int(input())
    if N > 4 or N < 1:
        print("none")
        break
    else:
        if N == 1:
            print("Seoul")
        elif N == 2:
            print("Washington")
        elif N == 3:
            print("Tokyo")
        else:
            print("Beijing")
