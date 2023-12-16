from datetime import datetime


class Car:
    current_year = datetime.now().year

    def __init__(self, brand, purchase_year, purchase_price):
        self.brand = brand
        self.purchase_year = purchase_year
        self.purchase_price = purchase_price
        self.total_distance = 0
        self.total_costs = 0
        self.update_current_year(purchase_year)

    def update_current_year(self, new_year):
        if new_year > Car.current_year:
            Car.current_year = new_year

    def set_year(self, new_year):
        if new_year > self.purchase_year:
            self.update_current_year(new_year)

    def drive(self, distance_driven, cost_per_kilometer):
        self.total_distance += distance_driven
        self.total_costs += distance_driven * cost_per_kilometer

    def add_expense(self, expense):
        self.total_costs += expense

    def distance_driven_by_car(self):
        return self.total_distance

    def current_value(self):
        depreciation_rate = 0.15
        years_passed = Car.current_year - self.purchase_year

        if years_passed <= 0:
            return self.purchase_price

        current_value = self.purchase_price
        for _ in range(years_passed):
            current_value *= (1 - depreciation_rate)
        return int(current_value)

    def cost_per_kilometer(self):
        if self.total_distance == 0:
            return 0.0
        total_cost = self.total_costs + \
            (self.purchase_price - self.current_value())
        return total_cost / self.total_distance

    def __str__(self):
        return f"{self.brand}: purchase year {self.purchase_year}, value {self.current_value()}"


if __name__ == "__main__":
    toyota = Car("Toyota", 2020, 10000)
    print(toyota)
    toyota.drive(100, 0.10)
    print(f"Distance driven with Toyota: {toyota.distance_driven_by_car()}")
    toyota.set_year(2021)
    print(f"Value of Toyota in 2021: {toyota.current_value()}")
    print(toyota)
    print(
        f"Cost per kilometer for Toyota in 2021: {toyota.cost_per_kilometer()}")
    toyota.set_year(2022)
    print(f"Value of Toyota in 2022: {toyota.current_value()}")
    bmw = Car("BMW", 2023, 20000)
    print(f"Value of Toyota after purchasing BMW: {toyota.current_value()}")
    bmw.drive(200, 0.12)
    bmw.drive(300, 0.13)
    print(f"Distance driven with BMW: {bmw.distance_driven_by_car()}")
    print(f"Cost per kilometer for BMW in 2023: {bmw.cost_per_kilometer()}")
    bmw.add_expense(1000)
    print(
        f"Cost per kilometer for BMW after a 1000 euro service: {bmw.cost_per_kilometer()}")
