class Product:
    def __init__(self, name: str,  weight:float, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__ (self):
        return f'{self.name},{ self.weight},{ self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(Shop.__file_name, 'r')
        products = file.read()
        file.close()
        return products.strip()

    def add(self, *products:Product):
        file = open(Shop.__file_name, 'a')
        old_products = self.get_products()
        for product in products:
            file.seek(0)
            if product.name in old_products:
                print(f'Продукт {product} уже есть в магазине')
            else:
                file.write(f'{product}\n')
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
