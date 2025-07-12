num = int(input())
result = "dog" if num == 1 else("cat" if num == 2 else("chick" if num == 3 else "I don't know."))
print("Number? ", end="")
print(result)