from order import Order

class Customer:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.orders = []

    def get_order_count(self):
        return len(self.orders)

    def get_total(self):
        return sum([order.get_total() for order in self.orders])

    def add_order(self, order):
        self.orders.append(order)

    def display_summary(self):
        print('Summary for customer \'{}\':\n'
              'Name: {}\nOrders: {}\nTotal: ${:.2f}'.format(self.id,
                                                       self.name,
                                                       self.get_order_count(),
                                                       self.get_total()))

    def display_receipts(self):
        print('Detailed receipts for customer \'{}\':'.format(self.id))
        print('Name: '.format(self.name))
        for order in self.orders:
            order.display_receipt()
