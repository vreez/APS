import sys; sys.stdin = open("1001.txt", "r")

while True:
    num, legs = map(int, input().split())
    if num == legs and num == 0:
        break
    else:
        if num <= 1000 and legs <= 4000:
            dog = (legs - (2 * num)) // 2
            chic = num - dog
            if dog >= 0 and chic >= 0 and (4 * dog + 2 * chic == legs):
                print(dog, chic)
            else:
                print(0)
        else:
            print("INPUT ERROR!")
