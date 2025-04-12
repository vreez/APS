a, b = input().split()

if a == "M":
    if int(b) >= 18:
        print("MAN")
    else:
        print("BOY")
else:
    if int(b) >= 18:
        print("WOMAN")
    else:
        print("GIRL")