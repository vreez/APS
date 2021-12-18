import sys; sys.stdin = open("4999.txt", "r")

jaehwan = list(input())
doctor = list(input())

aj = jaehwan.count("a")
ah = jaehwan.count("h")

dj = doctor.count("a")
dh = doctor.count("h")

if aj >= dj and ah == dh:
    print("go")
else:
    print("no")
