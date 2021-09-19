import sys; sys.stdin = open("1302.txt", "r")
import operator

N = int(input())
arr = []
for _ in range(N):
    arr.append(input())

books = {}
for i in range(N):
    if arr[i] not in books:
        books[arr[i]] = 1
    else:
        books[arr[i]] += 1
sortedList = sorted(books.items(), key=operator.itemgetter(1), reverse=True)
maxNum = sortedList[0][1]
result = []
for i in range(len(sortedList)):
    if sortedList[i][1] == maxNum:
        result.append(sortedList[i][0])

result.sort()
print(result[0])