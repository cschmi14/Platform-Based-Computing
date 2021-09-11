from person import Person


class Customer(Person):

    def __init__(self, first_name, last_name, orders):
        super().__init__(first_name, last_name)
        self.orders = orders

    def __str__(self):
        description = super().__str__()
        description += self.orders
        return description

    def add_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return self.orders
