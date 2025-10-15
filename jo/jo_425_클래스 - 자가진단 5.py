small = 500
s_name = ""
for i in range(5):
    name, height = input().split()
    if int(height) < small:
        small = int(height)
        s_name = name

print("{} {}".format(s_name, small))
