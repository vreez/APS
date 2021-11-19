import sys; sys.stdin = open("5218.txt", "r")

alpha = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

N = int(input())
for _ in range(N):
    first, second = input().split()
    M = len(first)
    nums = []
    for i in range(M):
        if second[i] >= first[i]:
            nums.append(alpha[second[i]] - alpha[first[i]])
        else:
            nums.append((alpha[second[i]] + 26) - alpha[first[i]])

    print('Distances: ', end="")
    for j in range(len(nums)):
        if j < len(nums) - 1:
            print(nums[j], end=" ")
        else:
            print(nums[j])
