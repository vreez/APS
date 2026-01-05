A, B, C, D = map(int, input().split())

bus = A + B
if bus <= D and C <= D:
    print("~.~")
elif bus > D and C > D:
    print("T.T")
elif bus <= D and C > D:
    print("Shuttle")
elif bus > D and C <= D:
    print("Walk")