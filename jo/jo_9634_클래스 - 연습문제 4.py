x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

print("점의 좌표는?(x, y) 점의 좌표는?(x, y) ", end="")
print("중심점의 위치 = ({}, {})".format(round((x1+x2)/2, 1), round((y1+y2)/2, 1)))