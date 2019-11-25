import os

#读取档案
def read_file(file_name):
    products = []
    products_1 = []
    with open(file_name, 'r') as f:
        for line in f:
            if '商品,价格' in line:
                continue
            s = line.strip().split(',')
            products.append(s)
            name, price = line.strip().split(',')
            products_1.append([name, price])
            print(s)
            print(name)
            print(products)
            print(products_1)
    return products

#让使用者输入，并存储到文件中
def user_input(products):
    while True:
        name = input("please input name")
        if name == 'q':
            break
        price = input("please input the price")
        # product =[]
        # product.append(name)
        # product.append(price)
        # product = [name,price]
        products.append([name, price])
    print(products)
    return products

#写入文件
def write_file(file_name, products):
    with open(file_name, 'w') as f:
        f.write('商品,价格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    file_name = 'products.csv'
    if os.path.isfile(file_name):
        print('yeah')
        products = read_file(file_name)
    else:
        print('no')
    products = user_input(products)
    write_file('products.csv',products)

if __name__ == '__main__':
    main()