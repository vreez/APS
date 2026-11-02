program = ["ADD", "DELETE", "SEARCH", "PRINT", "EXIT"]

while True:
    n = int(input())
    if n == 5:
        print(program[n-1])
        break
    elif n < 1 or n > 5:
        print("ERROR")
    else:
        print(program[n-1])