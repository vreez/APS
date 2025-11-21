c = list(map(int, input().split()))
e = list(map(int, input().split()))
score_c = 0
score_e = 1.5
for i in range(6):
    if i == 0:
        score_c += (c[i] * 13)
        score_e += (e[i] * 13)
    elif i == 1:
        score_c += (c[i] * 7)
        score_e += (e[i] * 7)
    elif i == 2:
        score_c += (c[i] * 5)
        score_e += (e[i] * 5)
    elif i == 3:
        score_c += (c[i] * 3)
        score_e += (e[i] * 3)
    elif i == 4:
        score_c += (c[i] * 3)
        score_e += (e[i] * 3)
    else:
        score_c += (c[i] * 2)
        score_e += (e[i] * 2)

if score_c > score_e:
    print("cocjr0208")
else:
    print("ekwoo")