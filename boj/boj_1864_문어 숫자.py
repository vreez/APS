import sys; sys.stdin = open("1864.txt", "r")
nums = {
    "-":0, "\\":1, "(":2, "@":3, "?":4, ">":5, "&":6, "%":7, "/":-1
}
while True:
    arr = list(input())
    if len(arr) == 1 and arr[0] == "#":
        break
    else:
        j = len(arr)-1
        total = 0
        for i in range(len(arr)):
            total += nums[arr[i]] * (8**j)
            j -= 1
    print(total)