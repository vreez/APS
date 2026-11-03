menu = ["NEW", "OPEN", "SAVE", "QUIT"]

while True:
    n = int(input())
    if n == 4:
        print(menu[n-1])
        break
    elif n < 1 or n > 4:
        print("AGAIN")
    else:
        print(menu[n-1])
        