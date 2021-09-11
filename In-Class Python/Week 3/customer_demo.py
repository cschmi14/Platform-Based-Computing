from customer import Customer


carter = Customer("carter", "schmidt", [4000])
carter.add_order(3000)
carter.add_order(2560)
print(carter.get_orders())

customers = []
with open("customers.txt") as file:
    for line in file:
        info = line.split()
        first_name = info[0]
        last_name = info[1]
        orders = []
        for i in range(2, len(info)):
            orders.append(info[i])
        customers.append(Customer(first_name, last_name, orders))

customers[2].say_hello()
print(customers[2].get_orders())
