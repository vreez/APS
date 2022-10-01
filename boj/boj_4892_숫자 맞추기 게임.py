import sys; sys.stdin = open("4892.txt", "r")

n = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    else:
        n1 = 3 * n0
        if n1 % 2:
            print("{}. {} ".format(n, "odd"), end="")
            n2 = n1 // 2
            n3 = 3 * n2
            n4 = n3 // 9
            print(n4)
        else:
            print("{}. {} ".format(n, "even"), end="")
            n2 = (n1 + 1) // 2
            n3 = 3 * n2
            n4 = n3 // 9
            print(n4)
        n += 1