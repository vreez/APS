n = int(input())
arr = [input() for _ in range(n)]
if arr.index("yonsei") <= arr.index("korea"):
    print("Yonsei Won!")
else:
    print("Yonsei Lost...")