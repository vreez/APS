T = int(input())
for t in range(1, T+1):
    s1 = input()
    s2 = input()

    i = 0
    j = 0
    M = len(s1)
    N = len(s2)
    while j < M and i < N:
        if s2[i] != s1[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M:
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t, 0))

