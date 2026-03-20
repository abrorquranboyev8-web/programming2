from abc import ABC, abstractmethod
class Calculator(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
    def compute(self, value):
        pass
    def describe(self, value):
        computed = self.compute(value)
        result = f"{self.name}: {value} -> {computed}"
        return result

class CaloriesToKilojoules(Calculator):
    def __init__(self):
        super().__init__("CaloriesToKilojoules")
    def compute(self, value):
        result = round(value * 4.184, 2)
        return result

class GramsToOunces(Calculator):
    def __init__(self):
        super().__init__("GramsToOunces")
    def compute(self, value):
        result = round(value * 0.035274, 2)
        return result

class CupsToMilliliters(Calculator):
    def __init__(self):
        super().__init__("CupsToMilliliters")
    def compute(self, value):
        result = round(value * 236.588, 2)
        return result

class CustomCalculator:
    def __init__(self, name, factor):
        self.name = name
        self.factor = factor
    def compute(self, value):
        result = round(value * self.factor, 2)
        return result
    def describe(self, value):
        computed = self.compute(value)
        result = f"{self.name}: {value} -> {computed}"
        return result

class CalculationLog:
    def __init__(self):
        self.entries = []
    def record(self, calc_name, original, computed):
        text = f"{calc_name}: {original} -> {computed}"
        self.entries.append(text)
    def show(self):
        for i in self.entries:
            print(i)

class NutritionLab:
    def __init__(self, name):
        self.name = name
        self.calculators = []
        self.log = CalculationLog()
    def add_calculator(self, calculator):
        self.calculators.append(calculator)
    def compute_all(self, value):
        print(f"=== {self.name} ===")
        for c in self.calculators:
            text = c.describe(value)
            print(text)
            computed = c.compute(value)
            self.log.record(c.name, value, computed)
    def show_log(self):
        print(f"--- Log for {self.name} ---")
        self.log.show()




lab = NutritionLab('Diet Clinic')
lab.add_calculator(CaloriesToKilojoules())
lab.add_calculator(GramsToOunces())
lab.add_calculator(CupsToMilliliters())
lab.add_calculator(CustomCalculator('TspsToMl', 4.929))

lab.compute_all(500)
print()
lab.compute_all(120)
print()
lab.show_log()

try:
    c = Calculator('test')
except TypeError:
    print('Cannot instantiate abstract class')










