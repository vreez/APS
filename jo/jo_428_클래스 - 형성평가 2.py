arr = []
for i in range(3):
    name, num, address = input().split()
    arr.append([name, num, address])

arr.sort(key=lambda x:x[0])

class person:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
p = person(arr[0][0], arr[0][1], arr[0][2])
print("name : {}".format(p.a))
print("tel : {}".format(p.b))
print("addr : {}".format(p.c))