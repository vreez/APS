import sys; sys.stdin = open("18198.txt", "r")

record = list(input())

result = {
    "A" : 0, "B" : 0
}
for i in range(len(record)):
    if record[i] == "A":
        result["A"] += int(record[i+1])
    elif record[i] == "B":
        result["B"] += int(record[i + 1])

if result["A"] > result["B"]:
    print("A")
else:
    print("B")