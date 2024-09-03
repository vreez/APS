import sys; sys.stdin = open("17293.txt", "r")

N = int(input())
num = N
while N != 0:
    if N > 1:
        if N-1>1:
            print("{} bottles of beer on the wall, {} bottles of beer.".format(N, N))
            print("Take one down and pass it around, {} bottles of beer on the wall.".format(N-1))
        else:
            print("{} bottles of beer on the wall, {} bottles of beer.".format(N, N))
            print("Take one down and pass it around, 1 bottle of beer on the wall.")
    elif N == 1:
        print("{} bottle of beer on the wall, {} bottle of beer.".format(N, N))
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    print()
    N -= 1
if N == 0:
    if num != 1:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, {} bottles of beer on the wall.".format(num))
    else:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, {} bottle of beer on the wall.".format(num))

