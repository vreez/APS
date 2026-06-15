N = int(input())
total = 0
for i in range(N):
    num = int(input())
    total += num

print("sum: {}".format(total))
print("avg: {:.1f}".format(total/N))