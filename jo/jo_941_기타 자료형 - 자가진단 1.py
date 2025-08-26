tp =  ('Forest', 'Ocean', 'Mountain', 'Plain')
N = int(input())
if N < 1 or N > 4:
    print("Input Error")
else:
    print(tp[N-1])