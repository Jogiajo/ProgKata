class ShoppingCart():
	def __init__(self):
		total = 0
		items = {}

	def add_item(self, item_name, quantity, price):
		total = total + price
		items[item_name] =  quantity

	def remove_item(self, item_name, quantity, price):
		total = total - price
		del d[item_name]

	def checkout(self, cash_paid):
		if cash_paid < total:
			return "Cash paid not enough"
		else:
			return (cash_paid - total)

class Shopping(ShoppingCart):
	def __init__(self):
		quantity = 100

	def remove_item(self):
		total = total - 1

