N = int(input())
li = {}
for i in range(N):
    a, b = input().split()
    li[a] = b
ctry = input()
if ctry in li:
    print(li[ctry])
else:
    print("Unknown Country")



