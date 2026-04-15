s, a = input().split()

if s == "M":
    if int(a) >= 19:
        print("MAN")
    else:
        print("BOY")
else:
    if int(a) >= 19:
        print("WOMAN")
    else:
        print("GIRL")