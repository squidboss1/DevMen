orders = [
["34587", "Learning Python, Mark Lutz", 4, 40.95],
["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95],
["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
]

calculated_orders = lambda order: (order[0], order[2] * order[3] if order[2] * order[3] >= 100 else order[2] * order[3] + 10)

invoice = list(map(calculated_orders, orders))

print(invoice)
