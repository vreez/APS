import sys; sys.stdin = open("15820.txt", "r")

s1, s2 = map(int, input().split())
sample = True
for _ in range(s1):
    ta, sa = map(int, input().split())
    if ta != sa:
        sample = False
        break
system = True
for _ in range(s2):
    ta, sa = map(int, input().split())
    if ta != sa:
        system = False
        break

if sample == True and system == True:
    print("Accepted")
elif sample == False:
    print("Wrong Answer")
elif sample == True and system == False:
    print("Why Wrong!!!")