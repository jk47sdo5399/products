products = []
while True:
    name = input("please input name")
    if name == 'q':
        break
    price = input("please input the price")
    # product =[]
    # product.append(name)
    # product.append(price)
    #product = [name,price]
    products.append([name,price])
print(products)

with open('products.csv', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1]+ '\n')

