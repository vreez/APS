name, grade = input().split()

class school:
    def __init__(self, i, j):
        self.i = i
        self.j = j
me = school("Jejuelementary", "6")
friends = school(name, grade)
print("{} grade in {} School".format(me.j, me.i))
print("{} grade in {} School".format(friends.j, friends.i))