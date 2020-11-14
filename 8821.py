import sys; sys.stdin = open("8821.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))

    cnt = 0
    note = []
    for i in range(len(arr)):
        if arr[i] not in note:
            note.append(arr[i])
            cnt += 1
        elif arr[i] in note:
            note.remove(arr[i])
            cnt -= 1

    print("#{} {}".format(tc, cnt))
