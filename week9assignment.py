from dataclasses import dataclass, field
@dataclass
class Component:
    name: str
    units: float
    price_per_unit: float

    def total_price(self) -> float:
        result = self.units * self.price_per_unit
        return result
    
@dataclass
class Assembly:
    title: str
    batch_size: int
    components: list = field(default_factory=list)
    total_price: float = field(init=False)

    def __post_init__(self):
        self._refresh()
    def _refresh(self):
        total = 0
        for c in self.components:
            total += c.total_price()
        self.total_price = total
    def add_component(self, component: Component):
        self.components.append(component)
        self._refresh()
    def price_per_item(self) -> float:
        result = self.total_price / self.batch_size
        return result
    def scale(self, new_batch_size: int):
        ratio = new_batch_size / self.batch_size
        for c in self.components:
            c.units = c.units * ratio
        self.batch_size = new_batch_size
        self._refresh()
    def display(self) -> str:
        text = f"{self.title} ({self.batch_size} items):\n"
        for c in self.components:
            text += f"  {c.name}: {c.units} units (${c.total_price()})\n"
        text += f"Per item: ${self.price_per_item()}"
        return text

a = Assembly("Drone", 8)
a.add_component(Component("Motor", 32.0, 15.0))
a.add_component(Component("Frame", 8.0, 45.0))
a.add_component(Component("Battery", 16.0, 25.0))

print(a.total_price)
print(a.price_per_item())
print(a.display())

a.scale(4)
print(a.display())