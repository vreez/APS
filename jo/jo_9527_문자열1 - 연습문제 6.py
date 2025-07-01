name, k, e, m = input().split()
s = int(k) + int(e) + int(m)
for _ in range(2):
    print("           name  kor  eng  mat  sum    avg ")
    print("     {}  {}    {}   {}  {}  {}".format(name, int(k), int(e), int(m), s, round(s/3, 2)))
    print()