arr = []
arr.append([5,8,10,6,4])
arr.append([11,20,1,13,2])
arr.append([7,9,14,22,3])

for i in range(3):
    for j in range(5):
        print("%2d"%(arr[i][j]), end="   ")
    print()