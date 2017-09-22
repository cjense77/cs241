class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def display(self):
        print('{} ({}) - ${}'.format(self.name,
                                     self.quantity,
                                     self.price))