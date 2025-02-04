class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def buy_product(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return f"{quantity} {self.name}(s) purchased. Remaining stock: {self.stock}"
        else:
            return "Insufficient stock."

product1 = Product("Laptop", 1000, 10)
print(product1.buy_product(3))
