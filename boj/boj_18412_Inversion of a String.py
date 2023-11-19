import sys; sys.stdin = open("18412.txt", "r")

N, A, B = map(int, input().split())
S = input()
new = S[A-1 : B][::-1]
front = S[:A-1]
back = S[B:]
ans = front + new + back
ans = S[0] + ans[1:-1] + S[N-1]

print(ans)
