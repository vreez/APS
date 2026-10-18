h = int(input())
a = int(input())

if h >= 140 and a >= 10:
    print("RIDE")
elif h >= 140 or a >= 10:
    print("WITH ADULT")
else:
    print("WAIT")