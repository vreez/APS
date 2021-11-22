import sys; sys.stdin = open("6996.txt", "r")

N = int(input())
for _ in range(N):
    a, b = input().split()
    arr1 = list(a)
    arr2 = list(b)
    if len(arr1) != len(arr2):
        print("{} & {} are NOT anagrams.".format(a, b))
    else:
        for i in range(len(arr2)):
            if arr2[i] in arr1:
                arr1.remove(arr2[i])
        if len(arr1) == 0:
            print("{} & {} are anagrams.".format(a, b))
        else:
            print("{} & {} are NOT anagrams.".format(a, b))