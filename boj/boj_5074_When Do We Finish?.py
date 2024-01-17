import sys; sys.stdin = open("5074.txt", "r")

while True:
    s, e = input().split()
    st, sm = map(int, s.split(":"))
    et, em = map(int, e.split(":"))
    if st == sm and sm == et and et == em and st == 0:
        break
    else:
        total = (st*60+sm) + (et*60+em)
        ad = total // 60 // 24
        at = total // 60 % 24
        am = total % 60

        if ad == 0:
            print("%02d:%02d" %(at, am))
        else:
            print("%02d:%02d +%d" %(at, am, ad))