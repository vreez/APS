import sys; sys.stdin = open("29751.txt", "r")

W, H = map(int, input().split())

ans = (W * H) / 2
print("{:.1f}".format(ans))