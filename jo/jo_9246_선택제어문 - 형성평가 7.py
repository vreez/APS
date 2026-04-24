A, B, C = map(int, input().split())

mx = A if (A > B and A > C) else (B if B > C else C)
mi = A if (A < B and A < C) else (B if B < C else C)

print(mx - mi )