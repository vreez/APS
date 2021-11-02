import sys; sys.stdin = open("2809.txt", "r")

N = int(input())

nums = []
nums2 = []
for i in range(1, int(N ** 0.5)+1):
    if N % i == 0:
        nums.append(i)
        if (N // i) != i:
            nums2.append(N // i)

reverse_nums2 = nums2[::-1]

total = nums + reverse_nums2
for i in range(len(total)):
    print(total[i], end=" ")
