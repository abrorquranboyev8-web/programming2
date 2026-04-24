class InventoryError(Exception):
    pass

class ProductNotFoundError(InventoryError):
    def __init__(self, product_name):
        self.product_name = product_name
        error_text = f"product not found: {product_name}"
        super().__init__(error_text)

class InsufficientStockError(InventoryError):
    def __init__(self, product_name, requested, available):
        self.product_name = product_name
        self.requested = requested
        self.available = available
        self.shortage = requested - available
        error_text = f"cannot sell {requested} of {product_name}: only {available} in stock, short by {self.shortage}"
        super().__init__(error_text)

class InvalidQuantityError(InventoryError):
    def __init__(self, quantity):
        self.quantity = quantity
        error_text = f"invalid quantity: {quantity}. must be positive"
        super().__init__(error_text)

class Warehouse:
    def __init__(self):
        self.products = {}
    
    def add_product(self, name, price, quantity):
        if quantity <= 0:
            raise InvalidQuantityError(quantity)
        if name in self.products:
            self.products[name]["quantity"] += quantity
            self.products[name]["price"] = price
        else:
            self.products[name] = {
                "price": price,
                "quantity": quantity
            }

    def sell(self, name, quantity):
        if quantity <= 0:
            raise InvalidQuantityError(quantity)
        try:
            product = self.products[name]
        except KeyError:
            raise ProductNotFoundError(name) from None
        if quantity > product["quantity"]:
            raise InsufficientStockError(name, quantity, product["quantity"])
        product["quantity"] -= quantity
        result = round(quantity * product["price"], 2)
        return result

    def total_value(self):
        total = 0
        for name in self.products:
            total += self.products[name]["price"] * self.products[name]["quantity"]
        result = round(total, 2)
        return result






wh = Warehouse()

wh.add_product("Laptop", 899.99, 10)
wh.add_product("Mouse", 25.50, 50)
wh.add_product("Keyboard", 45.00, 30)

print(f"total value: {wh.total_value()}")

sale = wh.sell("Laptop", 3)
print(f"sold 3 laptops for: {sale}")
print(f"total value: {wh.total_value()}")

wh.add_product("Mouse", 27.00, 20)
print(f"total value: {wh.total_value()}")

tests = [
    lambda: wh.sell("Monitor", 1),
    lambda: wh.sell("Laptop", 50),
    lambda: wh.add_product("Tablet", 199.99, -5),
]

for test in tests:
    try:
        test()
    except InventoryError as e:
        print(e)



