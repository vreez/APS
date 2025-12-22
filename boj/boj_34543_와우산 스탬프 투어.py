n = int(input())
w = int(input())

score = n*10
if n >= 3:
    score += 20
if n == 5:
    score += 50
if w > 1000:
    if score <= 15:
        score = 0
    else:
        score -= 15


print(score)