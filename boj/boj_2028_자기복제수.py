import sys; sys.stdin = open("2028.txt", "r")

N = int(input())
for _ in range(N):
    num = int(input())
    word_num = str(num)
    double = num * num
    word_double = str(double)

    if int(word_double[-len(word_num):]) == num:
        print("YES")
    else:
        print("NO")
