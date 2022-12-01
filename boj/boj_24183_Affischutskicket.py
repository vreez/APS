import sys; sys.stdin = open("24183.txt", "r")

a, b, c = map(int, input().split())
answer = ((0.229 * 0.324)*a*2 + (0.297*0.420)*b*2 + (0.210*0.297)*c)

print(format(answer, ".6f"))