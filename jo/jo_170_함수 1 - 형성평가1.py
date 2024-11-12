import sys; sys.stdin = open("170.txt", "r")

def func():
    for i in range(3):
        if i == 0:
            print("first")
        elif i == 1:
            print("second")
        else:
            print("third")
        print("@@@@@@@@@@")

func()