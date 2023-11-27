class Order:
    def __init__(self, order_id, name, price):
        self.id = order_id
        self.name = name
        self.price = price

class Manager:
    def __init__(self):
        self.orders_dict = {}

    def add_order(self, order):
        # Jeżeli zamówienie o danym ID już istnieje, zwiększ ilość w managerze
        if order.id in self.orders_dict:
            self.orders_dict[order.id] += 1

        # Jeżeli zamówienie o danym ID nie istnieje, dodaj nowe zamówienie do słownika
        else:
            self.orders_dict[order.id] = 1

    def remove_order(self, order_id):
        # Usuń jedno zamówienie o określonym ID
        if order_id in self.orders_dict and self.orders_dict[order_id] > 0:
            self.orders_dict[order_id] -= 1

            # Jeżeli ilość zamówień danego typu spadnie do zera, usuń klucz ze słownika
            if self.orders_dict[order_id] == 0:
                del self.orders_dict[order_id]
            print(f"Usunięto 1 zamówienie o ID {order_id}.")
        else:
            print(f"Nie ma zamówienia o ID {order_id} do usunięcia.")

manager = Manager()

order1 = Order(1, "Węgiel", 1500)
order2 = Order(2, "Koks", 900)

manager.add_order(order1)
manager.add_order(order2)
manager.add_order(order1)

print(f"Produkt 1 to: [{order1.name}], a Produkt 2 to: [{order2.name}].\nStan zamówień po dodaniu: {manager.orders_dict}.")

manager.remove_order(1)
manager.remove_order(2)

print(f"Stan zamówień po usunięciu: {manager.orders_dict}")
