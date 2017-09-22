from product import Product

class Order:
    def __init__(self):
        self.id = ''
        self.products = []

    def get_subtotal(self):
        return sum([product.get_total_price() for product in self.products])

    def get_tax(self):
        return self.get_subtotal() * 0.065

    def get_total(self):
        return self.get_subtotal() + self.get_tax()

    def add_product(self, product):
        self.products.append(product)

    def display_receipt(self):
        print('\nOrder: {}'.format(self.id))
        for product in self.products:
            product.display()
        print('Subtotal: ${}\nTax: ${}\nTotal: ${}'.format(self.get_subtotal(),
                                                        self.get_tax(),
                                                        self.get_total()))
