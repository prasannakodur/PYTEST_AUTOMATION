from collections import Counter
X = int(input("the total number of shoes the shop has: "))
sizes = list(map(int,input("list of shoe sizes: ").split()))
Customers = int(input("no of customers: "))
orders = []
print(X)
print(sizes)
print(Customers)
for i in range(Customers):
    x,y = map(int,input("the customer orders: ").split())
    orders.append({x:y})
print(orders)

size_count = Counter(sizes)
print(size_count)
list_prices = []

for order in orders:
    k,v = list(order.items())[0]
    if (k in size_count.keys()) & (size_count[k]>0):
        size_count[k] -= 1
        list_prices.append(v)
print(sum(list_prices))


