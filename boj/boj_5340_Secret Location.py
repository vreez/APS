import sys; sys.stdin = open("5340.txt", "r")

result = []
for i in range(6):
    arr = input()
    ans = len(arr)
    if arr[-1] == " ":
        ans -= 1
    result.append(ans)

print("Latitude {}:{}:{}".format(result[0], result[1], result[2]))
print("Longitude {}:{}:{}".format(result[3], result[4], result[5]))