import sys; sys.stdin = open("1873.txt", "r")

tank = ['^', 'v', '<', '>'] # 방향에 따른 전차의 모습을 저장
user_dir = {'U':0, 'D':1, 'L':2, 'R':3} # 0: 상, 1:하, 2:좌, 3: 우
dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)] # 문자열을 받음
    N = int(input())
    user_input = list(input())

    # print(arr)
    # print('--------')
    # print(user_input)
    x = y = dir = -1 # 초기값 설정

    for i in range(H):
        for j in range(W):
            if arr[i][j] in tank: # 이차 배열을 탐색하다 전차를 발견했을 경우
                x = i
                y = j
                dir = tank.index(arr[i][j]) # 전차가 바라보는 방향을 dir로 표시
                break
        # 위의 break는 내부 for문 밖에 빠져나가지 못하므로 외부의 for문까지 빠져나갈 수 있도록 초기값이 변화하면 for문을 빠져나가도록 설정
        if x != -1:
            break

    for n in range(N):
        if user_input[n] != 'S': # 포탄 발사를 하지 않고 방향을 바꾸는 경우
            dir = user_dir[user_input[n]] # 전차 방향 바꾸기
            arr[x][y] = tank[dir] # 바뀐 전차의 모습을 기록

            newX = x + dx[dir] # 네 방향을 탐색해야 하므로
            newY = y + dy[dir]

            if 0 <= newX < H and 0 <= newY < W and arr[newX][newY] == '.': # .이라면 한 칸 이동 가능
                arr[newX][newY] = tank[dir] # 한 칸 이동한 곳에 새롭게 바뀐 전차의 모습을 기록
                arr[x][y] = '.' # 전차가 있던 공간은 평지로 바뀜
                x, y = newX, newY # 전차가 있는 곳이 기준점

        else: # 포탄을 쏘는 경우
            newX = x + dx[dir] # 포탄은 해당 부분을 통과할 수 있는지 없는 지 한 칸씩 이동하며 확인해야 한다.
            newY = y + dy[dir]

            while 0 <= newX < H and 0 <= newY < W: # 범위를 벗어나지 않는다면 계속해서 포탄은 나아갈 수 있다.
                if arr[newX][newY] == '#': break # 강철벽을 만나면 더 이상 포탄은 이동할 수 없다.
                if arr[newX][newY] == '*': # 벽돌벽을 만나면 벽돌은 부서지고 평지가 된다.
                    arr[newX][newY] = '.'
                    break # 더 이상 포탄은 이동할 수 없다.
                newX += dx[dir] # 포탄은 벽을 만나지 않았다면 같은 방향으로 계속 한 칸씩 이동한다.
                newY += dy[dir]

    print("#{}".format(tc), end=" ")

    for i in range(H):
        for j in range(W):
            print(arr[i][j], end="")
        print()

