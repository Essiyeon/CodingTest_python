N = int(input())
dice = []
price = []

for _ in range (N):
    a,b,c = map(int, input().split())
    dice = [a,b,c]
    dice.sort()

    if dice.count(a) == 3:
        price.append(10000 + (a * 1000))
    elif dice.count(a) == 2 or dice.count(b) == 2:
        price.append(1000 + (dice[1]* 100))
    else:
        price.append(dice[2] * 100)

print(max(price))