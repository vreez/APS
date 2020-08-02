T = int(input())
numbers = list(map(int, input().split()))

a = sorted(numbers)[int(len(numbers)/2)]      
print(a)