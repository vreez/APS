en, eb = input().split()
yn, yb = input().split()

print("{} was born in {}".format(en, int(eb)))
print("{} was born in {}".format(yn, int(yb)))
print("{} is {} years older than {}".format(en, int(yb)-int(eb), yn))
