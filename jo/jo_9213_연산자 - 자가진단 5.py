a, b, c = True, False, False

print(not a)
print(a and b)
print(a or b)
print(a and (a or c))
print(a or (a and c))
print(not b or (a and not c))