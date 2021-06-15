import sys; sys.stdin = open("17608.txt", "r")

# input()대신 sys.stdin.readline() 값을 사용하면 시간초과를 해결할 수 있다.
N = int(sys.stdin.readline())
arr = list(int(sys.stdin.readline()) for _ in range(N))

count = 1
max_bar = arr[N-1]
for i in range(N-2, -1, -1):
    if arr[i] > max_bar:
        # 오른쪽부터 검사하며 맨 오른쪽에 위치한 막대의 길이보다 더 긴 막대를 만날 경우,
        # max_bar를 길이가 더 긴 막대의 값으로 변경한다.
        max_bar = arr[i]
        count += 1

print(count)