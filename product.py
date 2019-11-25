products = []
products_1 = []
with open('products.csv', 'r') as f:
    for line in f:
        if '商品,价格' in line :
            continue
        s = line.strip().split(',')
        products.append(s)
        name, price = line.strip().split(',')
        products_1.append([name,price])
        print (s)
        print (name)
        print (products)
        print (products_1)

#让使用者输入，并存储到文件中
# while True:
#     name = input("please input name")
#     if name == 'q':
#         break
#     price = input("please input the price")
#     # product =[]
#     # product.append(name)
#     # product.append(price)
#     #product = [name,price]
#     products.append([name,price])
# print(products)
#
# with open('products.csv', 'w') as f:
#     f.write('商品,价格\n')
#     for p in products:
#         f.write(p[0] + ',' + p[1]+ '\n')

