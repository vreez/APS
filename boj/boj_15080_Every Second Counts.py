import sys; sys.stdin = open("15080.txt", "r")

Ah, Am, As = map(int, input().split(" : "))
Bh, Bm, Bs = map(int, input().split(" : "))

total = 0
if Bs >= As:
    total += (Bs - As)
else:
    Bs = Bs + 60
    Bm -= 1
    total += (Bs - As)

if Bm >= Am:
    total += (Bm * 60 - Am * 60)
else:
    Bm = Bm + 60
    Bh -= 1
    total += (Bm * 60 - Am * 60)

if Bh >= Ah:
    total += (Bh * 3600 - Ah * 3600)
else:
    Bh = Bh + 24
    total += (Bh * 3600 - Ah * 3600)

print(total)

