N = int(input())
if 2024 <= N <= 100000:
    if N % 2024 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
