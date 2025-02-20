price = []
for _ in range(5):
  price.append(int(input()))

burger_price = []
for i in range(3):
  burger_price.append(price[i])

beverage_price = []
for i in range(3,5):
  beverage_price.append(price[i])

print(min(burger_price)+min(beverage_price)-50)