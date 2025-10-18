name, num, address = input().split()
class person:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
p = person(name, num, address)
print("name : {}".format(p.a))
print("tel : {}".format(p.b))
print("addr : {}".format(p.c))