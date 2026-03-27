def track_change(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[STOCK] {result}")
        return result
    return wrapper

class Ingredient:
    _all_ingredients = []
    def __init__(self, name, cost_per_unit, units):
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.units = units
        Ingredient._all_ingredients.append(self)

    @track_change
    def order(self, amount):
        self.units += amount
        result = f"{self.name}: ordered {amount}, now {self.units}"
        return result

    @track_change
    def use(self, amount):
        if amount > self.units:
            result = f"Not enough {self.name} in kitchen"
            return result
        self.units -= amount
        result = f"{self.name}: used {amount}, now {self.units}"
        return result

    def total_cost(self):
        value = self.cost_per_unit * self.units
        result = float(round(value, 2))
        return result

    @classmethod
    def from_order_form(cls, entry):
        parts = entry.split(":")
        name = parts[0]
        cost = float(parts[1])
        units = int(parts[2])
        result = cls(name, cost, units)
        return result

    @staticmethod
    def is_valid_code(code):
        if code.startswith("ING-") and code[4:].isdigit():
            return True
        return False

    @classmethod
    def kitchen_value(cls):
        total = 0
        for i in cls._all_ingredients:
            total += i.total_cost()
        result = float(round(total, 2))
        return result

i1 = Ingredient("Rice", 3.20, 60)
i2 = Ingredient.from_order_form("Olive Oil:15.75:8")

i1.order(15)
i1.use(50)
i1.use(100)
i2.use(3)

print(f"{i1.name}: cost = ${i1.total_cost()}")
print(f"{i2.name}: cost = ${i2.total_cost()}")

print(f"Valid code 'ING-012': {Ingredient.is_valid_code('ING-012')}")
print(f"Valid code 'FD-999': {Ingredient.is_valid_code('FD-999')}")
print(f"Kitchen total: ${Ingredient.kitchen_value()}")









