first = [list(input().split()) for _ in range(2)]
second = [list(input().split()) for _ in range(2)]

print("first array")
print("second array")

for i in range(2):
    for j in range(4):
        print(int(first[i][j]) * int(second[i][j]), end=" ")
    print()