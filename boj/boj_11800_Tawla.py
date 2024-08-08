import sys; sys.stdin = open("11800.txt", "r")

nickname = ["Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"]
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    if a != b:
        if (a == 6 and b == 5) or (a == 5 and b == 6):
            print("Case {}: {}".format(i+1, "Sheesh Beesh"))
        else:
            if a > b:
                print("Case {}: {} {}".format(i+1, nickname[a-1], nickname[b-1]))
            else:
                print("Case {}: {} {}".format(i + 1, nickname[b - 1], nickname[a - 1]))
    else:
        if a == 1:
            print("Case {}: {}".format(i+1, "Habb Yakk"))
        elif a == 2:
            print("Case {}: {}".format(i + 1, "Dobara"))
        elif a == 3:
            print("Case {}: {}".format(i + 1, "Dousa"))
        elif a == 4:
            print("Case {}: {}".format(i + 1, "Dorgy"))
        elif a == 5:
            print("Case {}: {}".format(i + 1, "Dabash"))
        else:
            print("Case {}: {}".format(i + 1, "Dosh"))