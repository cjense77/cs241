"""
File: order.py
Author: Colin Jensen

This file supplies an Order class with various methods
and member variables handle a customer's order.
"""

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
        print('Order: {}'.format(self.id))
        for product in self.products:
            product.display()
        print('Subtotal: ${:.2f}\nTax: ${:.2f}\nTotal: ${:.2f}'.format(self.get_subtotal(),
                                                        self.get_tax(),
                                                        self.get_total()))
