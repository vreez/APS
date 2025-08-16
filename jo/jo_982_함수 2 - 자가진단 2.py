month, day = map(int, input().split())

def func(month, day):
    if month == 1:
        if day >= 1 and day <= 31:
            print("OK!")
        else:
            print("BAD!")
    elif month == 2:
        if day >= 1 and day <= 29:
            print("OK!")
        else:
            print("BAD!")
    elif month == 3:
        if day >= 1 and day <= 31:
            print("OK!")
        else:
            print("BAD!")
    elif month == 4:
        if day >= 1 and day <= 30:
            print("OK!")
        else:
            print("BAD!")
    elif month == 5:
        if day >= 1 and day <= 31:
            print("OK!")
        else:
            print("BAD!")
    elif month == 6:
        if day >= 1 and day <= 30:
            print("OK!")
        else:
            print("BAD!")
    elif month == 7:
        if day >= 1 and day <= 31:
            print("OK!")
        else:
            print("BAD!")
    elif month == 8:
        if day >= 1 and day <= 31:
            print("OK!")
        else:
            print("BAD!")
    elif month == 9:
        if day >= 1 and day <= 30:
            print("OK!")
        else:
            print("BAD!")
    elif month == 10:
        if day >= 1 and day <= 31:
            print("OK!")
        else:
            print("BAD!")
    elif month == 11:
        if day >= 1 and day <= 30:
            print("OK!")
        else:
            print("BAD!")
    elif month == 12:
        if day >= 1 and day <= 31:
            print("OK!")
        else:
            print("BAD!")
    else:
        print("BAD!")

func(month, day)

